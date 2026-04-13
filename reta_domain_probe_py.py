#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python-nahe Referenz- und Inspektionshilfe für reta.
Dieses Skript spiegelt die wichtigsten JSON-/Probe-Kommandos von
`reta_domain_probe` auf Basis der Python-Referenzdaten in i18n/words.py.

Es greift nicht in die normale reta-CLI ein.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


def _prepare_imports() -> Path:
    here = Path(__file__).resolve()
    candidates = [
        here.parent,
        here.parent.parent,
        Path.cwd(),
    ]
    for base in candidates:
        if (base / "i18n" / "words.py").exists():
            sys.path.insert(0, str(base))
            sys.path.insert(0, str(base / "i18n"))
            return base
    raise SystemExit(
        "Konnte i18n/words.py nicht finden. "
        "Lege das Skript im Python-reta-Repo ab oder starte es von dort."
    )


REPO_ROOT = _prepare_imports()

from i18n.words import ParametersMain, paraNdataMatrix  # type: ignore  # noqa: E402


def canonical_main_alias_groups() -> List[Dict[str, object]]:
    groups = []
    for tup in ParametersMain:
        aliases = [str(x) for x in tup]
        if not aliases:
            continue
        groups.append({"canonical": aliases[0], "aliases": aliases})
    return groups


def _main_alias_map() -> Dict[str, str]:
    out: Dict[str, str] = {}
    for group in canonical_main_alias_groups():
        canonical = str(group["canonical"])
        for alias in group["aliases"]:  # type: ignore[index]
            out[str(alias)] = canonical
    return out


def parameter_alias_groups_for_main(main_name: str) -> List[Dict[str, object]]:
    main_canonical = resolve_main_alias(main_name)
    if main_canonical is None:
        return []

    groups: Dict[str, List[str]] = {}
    for entry in paraNdataMatrix:
        main_aliases = entry[0]
        parameter_aliases = entry[1]
        _datas = entry[2]
        main_aliases = tuple(str(x) for x in main_aliases)
        if not main_aliases:
            continue
        if main_aliases[0] != main_canonical:
            continue
        parameter_aliases = [str(x) for x in parameter_aliases]
        if not parameter_aliases:
            continue
        canonical_parameter = parameter_aliases[0]
        groups.setdefault(canonical_parameter, [])
        for alias in parameter_aliases:
            if alias not in groups[canonical_parameter]:
                groups[canonical_parameter].append(alias)

    return [
        {"canonical": canonical, "aliases": aliases}
        for canonical, aliases in sorted(groups.items(), key=lambda item: item[0])
    ]


def resolve_main_alias(main_name: str) -> Optional[str]:
    return _main_alias_map().get(main_name)


def resolve_parameter_alias(main_name: str, parameter_name: str) -> Optional[str]:
    for group in parameter_alias_groups_for_main(main_name):
        canonical = str(group["canonical"])
        aliases = [str(x) for x in group["aliases"]]  # type: ignore[index]
        if parameter_name in aliases:
            return canonical
    return None


def canonicalize_pair(main_name: str, parameter_name: str) -> Optional[Tuple[str, str]]:
    canonical_main = resolve_main_alias(main_name)
    if canonical_main is None:
        return None
    canonical_parameter = resolve_parameter_alias(canonical_main, parameter_name)
    if canonical_parameter is None:
        return None
    return canonical_main, canonical_parameter


def column_numbers_for_pair(main_name: str, parameter_name: str) -> List[int]:
    pair = canonicalize_pair(main_name, parameter_name)
    if pair is None:
        return []
    canonical_main, canonical_parameter = pair

    cols = set()
    for entry in paraNdataMatrix:
        main_aliases = entry[0]
        parameter_aliases = entry[1]
        datas = entry[2]
        main_aliases = tuple(str(x) for x in main_aliases)
        parameter_aliases = tuple(str(x) for x in parameter_aliases)
        if not main_aliases or not parameter_aliases:
            continue
        if main_aliases[0] == canonical_main and parameter_aliases[0] == canonical_parameter:
            cols |= {int(x) for x in datas}
    return sorted(cols)


def reverse_map_canonical_pairs() -> Dict[int, List[Tuple[str, str]]]:
    out: Dict[int, List[Tuple[str, str]]] = {}
    for entry in paraNdataMatrix:
        main_aliases = entry[0]
        parameter_aliases = entry[1]
        datas = entry[2]
        main_aliases = tuple(str(x) for x in main_aliases)
        parameter_aliases = tuple(str(x) for x in parameter_aliases)
        if not main_aliases or not parameter_aliases:
            continue
        pair = (main_aliases[0], parameter_aliases[0])
        for col in datas:
            col = int(col)
            out.setdefault(col, [])
            if pair not in out[col]:
                out[col].append(pair)

    for col in out:
        out[col] = sorted(out[col], key=lambda x: (x[0], x[1]))
    return dict(sorted(out.items(), key=lambda x: x[0]))


def exact_meta_for_column(column_number: int) -> List[Dict[str, object]]:
    matches: List[Dict[str, object]] = []
    for entry in paraNdataMatrix:
        main_aliases = entry[0]
        parameter_aliases = entry[1]
        datas = entry[2]
        if column_number not in datas:
            continue
        main_aliases = [str(x) for x in main_aliases]
        parameter_aliases = [str(x) for x in parameter_aliases]
        if not main_aliases or not parameter_aliases:
            continue
        matches.append(
            {
                "column_number": int(column_number),
                "parameter_main": main_aliases[0],
                "parameter_main_aliases": main_aliases,
                "parameter": parameter_aliases[0],
                "parameter_aliases": parameter_aliases,
            }
        )
    return sorted(matches, key=lambda x: (str(x["parameter_main"]), str(x["parameter"])))


def main_json(main_name: str) -> Dict[str, object]:
    canonical_main = resolve_main_alias(main_name)
    if canonical_main is None:
        raise SystemExit(f"Unbekannter Hauptparameter: {main_name}")

    aliases: List[str] = []
    for group in canonical_main_alias_groups():
        if group["canonical"] == canonical_main:
            aliases = [str(x) for x in group["aliases"]]  # type: ignore[index]
            break

    all_columns = set()
    pairs = []

    for group in parameter_alias_groups_for_main(canonical_main):
        canonical_parameter = str(group["canonical"])
        parameter_aliases = [str(x) for x in group["aliases"]]  # type: ignore[index]
        cols = column_numbers_for_pair(canonical_main, canonical_parameter)
        if cols:
            all_columns |= set(cols)
            pairs.append(
                {
                    "parameter": canonical_parameter,
                    "aliases": parameter_aliases,
                    "columns": cols,
                }
            )

    return {
        "main": canonical_main,
        "aliases": aliases,
        "columns": sorted(all_columns),
        "pairs": pairs,
    }


def pairs_json(main_name: str) -> List[Dict[str, object]]:
    canonical_main = resolve_main_alias(main_name)
    if canonical_main is None:
        raise SystemExit(f"Unbekannter Hauptparameter: {main_name}")

    out = []
    for group in parameter_alias_groups_for_main(canonical_main):
        canonical_parameter = str(group["canonical"])
        cols = column_numbers_for_pair(canonical_main, canonical_parameter)
        if cols:
            out.append(
                {
                    "main": canonical_main,
                    "parameter": canonical_parameter,
                    "columns": cols,
                }
            )
    return out


def pair_json(main_name: str, parameter_name: str) -> Dict[str, object]:
    pair = canonicalize_pair(main_name, parameter_name)
    if pair is None:
        raise SystemExit(f"Unbekanntes Paar: {main_name} / {parameter_name}")

    canonical_main, canonical_parameter = pair
    main_aliases = []
    for group in canonical_main_alias_groups():
        if group["canonical"] == canonical_main:
            main_aliases = [str(x) for x in group["aliases"]]  # type: ignore[index]
            break

    parameter_aliases = []
    for group in parameter_alias_groups_for_main(canonical_main):
        if group["canonical"] == canonical_parameter:
            parameter_aliases = [str(x) for x in group["aliases"]]  # type: ignore[index]
            break

    return {
        "input_main": main_name,
        "input_parameter": parameter_name,
        "canonical_main": canonical_main,
        "canonical_parameter": canonical_parameter,
        "main_aliases": main_aliases,
        "parameter_aliases": parameter_aliases,
        "columns": column_numbers_for_pair(canonical_main, canonical_parameter),
    }


def column_json(column_number: int) -> Dict[str, object]:
    reverse = reverse_map_canonical_pairs()
    pairs = [{"main": main, "parameter": parameter} for main, parameter in reverse.get(column_number, [])]
    return {
        "column_number": int(column_number),
        "matches": exact_meta_for_column(column_number),
        "summary_pairs": pairs,
    }


def help_text(program_name: str) -> str:
    return f"""{program_name} - Python-Referenz- und Inspektionshilfe für reta

Aufruf:
  {program_name} -h
  {program_name} --help
  {program_name} mains
  {program_name} params <hauptparameter>
  {program_name} pairs <hauptparameter>
  {program_name} pairs-json <hauptparameter>
  {program_name} main-columns <hauptparameter>
  {program_name} main-json <hauptparameter>
  {program_name} pair <hauptparameter> <unterparameter>
  {program_name} pair-json <hauptparameter> <unterparameter>
  {program_name} column <spaltennummer>
  {program_name} column-json <spaltennummer>
  {program_name} reverse <spaltennummer>

Befehle:
  mains
      Zeigt alle kanonischen Oberkategorien und ihre Aliase.

  params <hauptparameter>
      Zeigt alle kanonischen Unterkategorien und ihre Aliase.

  pairs <hauptparameter>
      Zeigt alle kanonischen Paare mit direkten Spalten.

  pairs-json <hauptparameter>
      Wie pairs, aber als JSON.

  main-columns <hauptparameter>
      Zeigt die Vereinigungsmenge direkter Spalten dieses Hauptparameters.

  main-json <hauptparameter>
      Gesamtansicht eines Hauptparameters als JSON.

  pair <hauptparameter> <unterparameter>
      Kanonisiert das Paar und zeigt die direkten Spalten.

  pair-json <hauptparameter> <unterparameter>
      Wie pair, aber als JSON.

  column <spaltennummer>
      Zeigt die direkten Python-Metaeinträge einer Spalte.

  column-json <spaltennummer>
      Wie column, aber als JSON.

  reverse <spaltennummer>
      Zeigt nur die kanonischen Rückwärts-Paare einer Spalte.
"""


def print_json(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, separators=(",", ":")))


def main(argv: Sequence[str]) -> int:
    program_name = Path(argv[0]).name if argv else "reta_domain_probe_py.py"

    if len(argv) <= 1 or argv[1] in {"-h", "--help", "help"}:
        print(help_text(program_name))
        return 0

    cmd = argv[1]

    if cmd == "mains":
        for group in canonical_main_alias_groups():
            print(f'{group["canonical"]} => {", ".join(group["aliases"])}')
        return 0

    if cmd == "params":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} params <hauptparameter>")
        for group in parameter_alias_groups_for_main(argv[2]):
            print(f'{group["canonical"]} => {", ".join(group["aliases"])}')
        return 0

    if cmd == "pairs":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} pairs <hauptparameter>")
        canonical_main = resolve_main_alias(argv[2])
        if canonical_main is None:
            raise SystemExit(f"Unbekannter Hauptparameter: {argv[2]}")
        for group in parameter_alias_groups_for_main(canonical_main):
            cols = column_numbers_for_pair(canonical_main, str(group["canonical"]))
            if cols:
                print(f"{canonical_main} / {group['canonical']} => {cols}")
        return 0

    if cmd == "pairs-json":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} pairs-json <hauptparameter>")
        print_json(pairs_json(argv[2]))
        return 0

    if cmd == "main-columns":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} main-columns <hauptparameter>")
        data = main_json(argv[2])
        print(f"main_columns={data['columns']}")
        return 0

    if cmd == "main-json":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} main-json <hauptparameter>")
        print_json(main_json(argv[2]))
        return 0

    if cmd == "pair":
        if len(argv) != 4:
            raise SystemExit(f"Erwartet: {program_name} pair <hauptparameter> <unterparameter>")
        pair = canonicalize_pair(argv[2], argv[3])
        if pair is None:
            raise SystemExit(f"Unbekanntes Paar: {argv[2]} / {argv[3]}")
        print(f"canonical={pair[0]} / {pair[1]}")
        print(f"columns={column_numbers_for_pair(pair[0], pair[1])}")
        return 0

    if cmd == "pair-json":
        if len(argv) != 4:
            raise SystemExit(f"Erwartet: {program_name} pair-json <hauptparameter> <unterparameter>")
        print_json(pair_json(argv[2], argv[3]))
        return 0

    if cmd == "column":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} column <spaltennummer>")
        column_number = int(argv[2])
        matches = exact_meta_for_column(column_number)
        if not matches:
            raise SystemExit(f"Unbekannte oder nicht-direkte Spalte: {column_number}")
        for match in matches:
            print(f"{column_number} => {match}")
        reverse = reverse_map_canonical_pairs()
        print(f"summary_pairs={reverse.get(column_number, [])}")
        return 0

    if cmd == "column-json":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} column-json <spaltennummer>")
        print_json(column_json(int(argv[2])))
        return 0

    if cmd == "reverse":
        if len(argv) != 3:
            raise SystemExit(f"Erwartet: {program_name} reverse <spaltennummer>")
        reverse = reverse_map_canonical_pairs()
        print(f"summary_pairs={reverse.get(int(argv[2]), [])}")
        return 0

    raise SystemExit(f"Unbekannter Befehl: {cmd}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from collections import namedtuple
from itertools import zip_longest

import html2text

from tableHandling import (Enum, Iterable, OutputSyntax, Tables, Union, alxp,
                           bbcode, bbCodeSyntax, cliout, copy, csv, csvSyntax,
                           deepcopy, getTextWrapThings, htmlSyntax, infoLog,
                           markdownSyntax, math, os, output, primCreativity,
                           primzahlvielfachesuniversum, re, shellRowsAmount,
                           sys, x)

parser = bbcode.Parser()
parser.add_simple_formatter("hr", "<hr />", standalone=True)
parser.add_simple_formatter("sub", "<sub>%(value)s</sub>")
parser.add_simple_formatter("sup", "<sup>%(value)s</sup>")


def render_color(tag_name, value, options, parent, context):
    return '<span style="color:%s;">%s</span>' % (tag_name, value)


# print(os.path.dirname(__file__))
for color in ("red", "blue", "green", "yellow", "black", "white"):
    parser.add_formatter(color, render_color)
# puniverseprims = {
#     couldBePrimeNumber if primCreativity(couldBePrimeNumber) == 1 else None
#     for couldBePrimeNumber in range(2, 1025)
# } - {
#     None,
# }
#


class Program:
    def produceAllSpaltenNumbers(self, neg=""):
        global shellRowsAmount

        def resultingSpaltenFromTuple(tupl: tuple, neg, paraValue=None) -> tuple:
            x("TTT", paraValue)
            for i, eineSpaltenArtmitSpaltenNummern in enumerate(tupl):
                """
                Die Variable self.tables.spalteGestirn braucht man gar nicht mehr !!!
                """
                # if (
                #     i == 4
                #     and type(eineSpaltenArtmitSpaltenNummern[0]) is bool
                #     and eineSpaltenArtmitSpaltenNummern[0]
                # ):
                #     self.tables.spalteGestirn = True
                x("___", eineSpaltenArtmitSpaltenNummern)
                if (
                    type(eineSpaltenArtmitSpaltenNummern) in [list, tuple]
                    and len(eineSpaltenArtmitSpaltenNummern) > 0
                ):
                    if type(eineSpaltenArtmitSpaltenNummern[0]) is bool:
                        eineSpaltenArtmitSpaltenNummern = set(
                            eineSpaltenArtmitSpaltenNummern
                        )
                    elif type(eineSpaltenArtmitSpaltenNummern[0]) in [tuple, list]:
                        eineSpaltenArtmitSpaltenNummern = set(
                            eineSpaltenArtmitSpaltenNummern[0]
                        )
                if i == 2 and type(eineSpaltenArtmitSpaltenNummern) in [list, tuple]:
                    self.spaltenArtenKey_SpaltennummernValue[
                        (len(neg), 2)
                    ] |= eineSpaltenArtmitSpaltenNummern[0](paraValue)
                else:
                    x("_1", type(eineSpaltenArtmitSpaltenNummern))
                    x(
                        "_2",
                        type(self.spaltenArtenKey_SpaltennummernValue[(len(neg), i)]),
                    )
                    self.spaltenArtenKey_SpaltennummernValue[
                        (len(neg), i)
                    ] |= eineSpaltenArtmitSpaltenNummern
            return self.spaltenArtenKey_SpaltennummernValue

        def spalten_removeDoublesNthenRemoveOneFromAnother():
            for el2Type in range(
                int(len(self.spaltenArtenKey_SpaltennummernValue) / 2)
            ):
                self.spaltenArtenKey_SpaltennummernValue[(0, el2Type)] -= (
                    self.spaltenArtenKey_SpaltennummernValue[(0, el2Type)]
                    & self.spaltenArtenKey_SpaltennummernValue[(1, el2Type)]
                )
            for el2Type in range(
                int(len(self.spaltenArtenKey_SpaltennummernValue) / 2)
            ):
                self.spaltenArtenKey_SpaltennummernValue[
                    (0, el2Type)
                ] -= self.spaltenArtenKey_SpaltennummernValue[(1, el2Type)]
                self.spaltenArtenKey_SpaltennummernValue.pop((1, el2Type))

        # def notNormalParameters(parameter, parametervalue, tables):
        #     if parameter == "bedeutung" and parametervalue in [
        #         "gestirn",
        #         "mond",
        #         "sonne",
        #         "planet",
        #     ]:
        #         tables.spalteGestirn = True

        # self.intoParameterDatatype
        mainParaCmds: dict = {
            "zeilen": 0,
            "spalten": 1,
            self.tables.getCombis.parameterName: 2,
            "ausgabe": 3,
            "debug": None,
            "h": None,
            "help": None,
        }
        # mainParaCmds2: dict = {
        #    0: "zeilen",
        #    1: "spalten",
        #    2: "kombination",
        #    3: "ausgabe",
        # }
        lastMainCmd: int = -1
        # kombiSpalten = set()
        # ordinarySpalten = set()
        for cmd in self.argv[1:]:
            if len(cmd) > 2 and cmd[0] == "-" and cmd[1] != "-":
                if cmd[1:] in mainParaCmds.keys():
                    lastMainCmd = mainParaCmds[cmd[1:]]
                elif len(neg) == 0:
                    cliout(
                        'Der Haupt-Paramaeter "'
                        + cmd
                        + '" existiert hier nich als Befehl!'
                        + " Es ist nur möglich: -"
                        + str(", -".join(list(mainParaCmds.keys())))
                    )
            elif cmd[:2] == "--":
                if lastMainCmd == mainParaCmds["spalten"]:
                    cmd = cmd[2:]
                    eq = cmd.find("=")
                    if cmd[:7] == "breite=" and len(neg) == 0:
                        if cmd[7:].isdecimal():
                            breite = abs(int(cmd[7:]))
                            if breite == 0:
                                shellRowsAmount = 0
                            self.tables.textWidth = breite
                            self.breiteORbreiten = True
                    elif cmd[:8] == "breiten=" and len(neg) == 0:
                        self.tables.breitenn = []
                        for breite in cmd[8:].split(","):
                            if breite.isdecimal():
                                self.tables.breitenn += [int(breite)]
                                self.breiteORbreiten = True
                    elif cmd == "keinenummerierung" and len(neg) == 0:
                        self.tables.nummeriere = False
                    elif eq != -1:
                        for oneOfThingsAfterEqSign in cmd[eq + 1 :].split(","):
                            if (
                                len(oneOfThingsAfterEqSign) > 0
                                and oneOfThingsAfterEqSign[0] == "-"
                            ):
                                oneOfThingsAfterEqSign = oneOfThingsAfterEqSign[1:]
                                yes1 = True if neg == "-" else False
                            else:
                                yes1 = True if len(neg) == 0 else False
                            if yes1:
                                try:
                                    # notNormalParameters(
                                    #    cmd[:eq],
                                    #    oneOfThingsAfterEqSign,
                                    #    self.tables,
                                    # )
                                    x("geht villeicht 1:", cmd[:eq])
                                    resultingSpaltenFromTuple(
                                        self.paraDict[
                                            (cmd[:eq], oneOfThingsAfterEqSign)
                                        ],
                                        neg,
                                        oneOfThingsAfterEqSign,
                                    )
                                    alxp("geht 1:")
                                    alxp((cmd[:eq], oneOfThingsAfterEqSign))
                                except KeyError:
                                    alxp((cmd[:eq], oneOfThingsAfterEqSign))
                                    cliout(
                                        'Der Unter-Paramaeter "--'
                                        + cmd[:eq]
                                        + '" mit dem Textwert "'
                                        + oneOfThingsAfterEqSign
                                        + '" existiert hier nicht als Befehl für Haupt-Parameter'
                                        + " -spalten"
                                        + " !"
                                        + " Es ist nur möglich:\n--"
                                        + str(
                                            ", --".join(
                                                tuple(
                                                    set(
                                                        key[0]
                                                        for key in self.paraDict.keys()
                                                    )
                                                )
                                            )
                                        )
                                        + ", --breiten, --breite"
                                        + "\nmit dem Werten dahinter:\n"
                                        + str(
                                            ",".join(
                                                tuple(
                                                    set(
                                                        key[1]
                                                        for key in self.paraDict.keys()
                                                    )
                                                )
                                            )
                                        )
                                    )

                    else:
                        try:
                            if (cmd[-1] == "-" and neg == "-") != (
                                len(neg) == 0 and cmd[-1] != "-"
                            ):
                                if len(cmd) > 0 and cmd[-1] == "-" and len(neg) > 0:
                                    cmd = cmd[:-1]

                                x("TT1", self.paraDict[(cmd, "")])
                                resultingSpaltenFromTuple(self.paraDict[(cmd, "")], neg)
                                x("TT2", cmd)

                        except KeyError:
                            cliout(
                                'Der Unter-Paramaeter "--'
                                + cmd
                                + '" existiert hier nich als Befehl für Haupt-Parameter'
                                + " -spalten"
                                + " !"
                                + " Es ist nur möglich: --"
                                + str(
                                    ", --".join(
                                        tuple(
                                            set(key[0] for key in self.paraDict.keys())
                                        )
                                    )
                                )
                                + ", --keinenummerierung"
                            )

                elif lastMainCmd == mainParaCmds[self.tables.getCombis.parameterName]:
                    if cmd[:6] == "--was=":
                        for oneKombiSpalte in cmd[6:].split(","):
                            if len(oneKombiSpalte) > 0 and oneKombiSpalte[0] == "-":
                                oneKombiSpalte = oneKombiSpalte[1:]
                                yes1 = True if neg == "-" else False
                            else:
                                yes1 = True if len(neg) == 0 else False
                            if yes1:
                                try:
                                    resultingSpaltenFromTuple(
                                        (
                                            set(),
                                            set(),
                                            set(),
                                            {
                                                self.kombiReverseDict[oneKombiSpalte],
                                            },
                                        ),
                                        neg,
                                    )
                                    alxp("geht 2:")
                                    # kombiSpalten |= {self.kombiReverseDict[oneKombiSpalte]}
                                    pass
                                except KeyError:
                                    cliout(
                                        'Die Kombispalte "'
                                        + oneKombiSpalte
                                        + '" existiert so nicht als Befehl.'
                                    )

                    else:
                        cliout(
                            'kein Unter-Parameter "--was=" angegeben für Hauptparameter --kombination'
                        )
                elif lastMainCmd not in mainParaCmds.values():
                    cliout(
                        "Es muss ein Hauptparameter, bzw. der richtige, gesetzt sein, damit ein"
                        + ' Nebenparameter, wie möglicherweise: "'
                        + cmd
                        + '" ausgeführt werden kann. Hauptparameter sind: -'
                        + " -".join(mainParaCmds)
                    )
        if len(neg) == 0:
            self.produceAllSpaltenNumbers("-")
            # alxp("zusammen")
            # alxp(self.spaltenArtenKey_SpaltennummernValue)
            spalten_removeDoublesNthenRemoveOneFromAnother()
            # alxp("zusammen2")
            # alxp(self.spaltenArtenKey_SpaltennummernValue)

    def storeParamtersForColumns(self):
        # global puniverseprims

        def intoParameterDatatype(
            parameterMainNames: tuple, parameterNames: tuple, datas: tuple
        ) -> tuple:
            """Speichert einen Parameter mit seinem DatenSet
            in 2 Datenstrukturen (die beides kombinieren 2x2)
            Diese werden jedoch nur zurück gegeben und nicht in der Klasse gespeichert.
            @return: alle Hauptparamter| alle Nebenparamter zu nur einem
            Hauptparameter ergibt Mengen an Spalten | enthält alle Haup- und
            Nebenparameter keys sind Spalten der Tabelle
            """
            paraMainDict = {}
            for name in parameterMainNames:
                paraMainDict[name] = parameterNames
            paraDict = {}
            for name1 in parameterMainNames:
                for name2 in parameterNames:
                    paraDict[(name1, name2)] = datas
                if len(parameterNames) == 0:
                    paraDict[(name1, "")] = datas
            dataDicts: tuple = ({}, {}, {}, {})
            for i, d in enumerate(datas):
                for dd in d:
                    for parameterMainName in parameterMainNames:
                        for parameterName in (
                            parameterNames if len(parameterNames) > 0 else ("",)
                        ):
                            x("PANAME", parameterMainName)
                            x("PANAME", parameterName)
                            if i == 4 and (type(dd) is bool or type(dd[0]) is bool):
                                dataDicts[3][("bool", 0)] = (
                                    parameterMainName,
                                    parameterName,
                                )
                            elif i == 2 and type(dd) not in [tuple, int]:
                                dataDicts[i][
                                    (
                                        int(parameterName)
                                        if parameterName.isdecimal()
                                        else parameterName
                                        if len(parameterNames) > 0
                                        else None
                                    )
                                ] = [(parameterMainName, parameterName)]
                            else:
                                try:
                                    x("DIES", i)
                                    x("DIES", dd)
                                    x("DIES", dataDicts[i][dd])

                                    dataDicts[i][dd] += [
                                        (parameterMainName, parameterName)
                                    ]
                                #            if dd == 0:
                                #                alxp("funktionierte")
                                #                alxp(i)
                                #                alxp(dataDicts[i][dd])
                                #                alxp(parameterName)
                                except KeyError:
                                    dataDicts[i][dd] = [
                                        (parameterMainName, parameterName)
                                    ]
                        #             if dd == 0:
                        #                 alxp("funktionierte nicht")
                        #                 alxp(i)
                        #                 alxp(dataDicts[i][dd])
                        #                 alxp(parameterName)
            x("dadaDick", dataDicts)
            x("PARA", paraDict)
            return paraMainDict, paraDict, dataDicts

        def mergeParameterDicts(
            paraMainDict1: dict,
            paraDict1: dict,
            dataDicts1: list,
            paraMainDict2: dict,
            paraDict2: dict,
            dataDicts2: list,
        ) -> tuple:
            """Merged die beiden 2x2 Datenstrukturen und speichert diese
            in die Klasse und gibt sie dennoch auch mit return zurück
            @param paraMainDict: Hauptparameter in der Kommandozeile
            hat als Werte die Nebenparameter und keys sind die Hauptparamter
            @param paraDict: Nebenparamteter in der Kommandozeile
            hat als Werte die Spaltennummern dazugehörig
            @param dataDicts: die beiden Parameter sagen welche Spaltennummern es
            sein werden
            @return: Spaltennummer sagt welche Parameter es ingesamt dazu sind | die
            beiden Parameter sagen, welche Spalten es alle sind."""
            paraMainDict1 = {**paraMainDict1, **paraMainDict2}
            paraDict1 = {**paraDict1, **paraDict2}
            dataDicts3 = deepcopy(dataDicts1)
            # alxp(dataDicts3[0])
            # alxp(dataDicts2[0])
            for i, (dict1, dict2) in enumerate(zip_longest(dataDicts1, dataDicts2)):
                if type(dict1) is dict and type(dict2) is dict:
                    if len(dataDicts3[i].keys()) == 0:
                        dataDicts3[i] = dataDicts2[i]
                    else:
                        for key1, value1 in dict1.items():
                            for key2, value2 in dict2.items():
                                if key2 == key1:
                                    x("DING1", dataDicts3[i][key1])
                                    x("DING2", value2)
                                    dataDicts3[i][key1] += value2
                                elif key2 not in dataDicts3[i].keys():
                                    x("DONG", value2)
                                    dataDicts3[i][key2] = value2
            # alxp(dataDicts3)
            return paraDict1, dataDicts3

        Program.ParametersMain: namedtuple = namedtuple(
            "ParametersMain",
            "religionen galaxie strukturgroesse universum wirtschaft menschliches procontra licht bedeutung symbole primzahlvielfachesuniversum konzept inkrementieren operationen alles",
        )
        Program.ParametersMain = Program.ParametersMain(
            (
                "religionen",
                "religion",
            ),
            (
                "galaxie",
                "alteschriften",
                "kreis",
                "galaxien",
                "kreise",
            ),
            (
                "groessenordnung",
                "strukturgroesse",
                "groesse",
                "stufe",
                "organisationen",
            ),
            (
                "universum",
                "transzendentalien",
                "strukturalien",
            ),
            ("wirtschaft",),
            ("menschliches",),
            (
                "procontra",
                "dagegendafuer",
            ),
            ("licht",),
            ("bedeutung",),
            ("symbole",),
            primzahlvielfachesuniversum,
            (
                "konzept",
                "konzepte",
            ),
            ("inkrementieren",),
            ("operationen",),
            ("alles"),
        )
        allowedPrimNumbersForCommand = tuple(
            (
                str(num)
                for num in tuple(
                    set(
                        (
                            num if primCreativity(num) == 1 else None
                            for num in range(2, 32)
                        )
                    )
                    - {None}
                )
            )
        )

        paraNdataMatrix = [
            (
                Program.ParametersMain.operationen,
                (
                    "halbierung",
                    "halbierungen",
                ),
                {86},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "prophet",
                    "archon",
                    "religionsgründertyp",
                    "religionsgruendertyp",
                ),
                {72},
            ),
            (Program.ParametersMain.religionen, ("sternpolygon",), {0, 6, 36}),
            (
                Program.ParametersMain.religionen,
                (
                    "babylon",
                    "dertierkreiszeichen",
                ),
                {0, 36},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "vergleich",
                    "sternpolygonvsgleichfoermiges",
                    "vergleichnvs1divn",
                ),
                {87},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "messias",
                    "heptagramm",
                    "hund",
                    "messiase",
                    "messiasse",
                ),
                {7},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "gleichfoermigespolygon",
                    "gleichförmigespolygon",
                    "nichtsternpolygon",
                    "polygon",
                ),
                {16, 37},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "vertreterhoehererkonzepte",
                    "galaxien",
                    "galaxie",
                    "schwarzesonne",
                    "schwarzesonnen",
                    "universum",
                    "universen",
                    "kreis",
                    "kreise",
                    "kugel",
                    "kugeln",
                ),
                {23},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "babylon",
                    "tierkreiszeichen",
                ),
                {1, 2},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "thomas",
                    "thomasevangelium",
                ),
                {0, 3},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "analytischeontologie",
                    "ontologie",
                ),
                {84},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                ("groesse", "gross", "strukturgroesse"),
                {4, 21, 54},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                ("organisationen", "organisation"),
                {82},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                ("politik", "politischesysteme"),
                {83},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "analytische_ontologie ",
                    "ontologie_",
                ),
                {84},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "transzendentalien",
                    "transzendentalie",
                    "strukturalien",
                    "alien",
                    "existenzialien",
                    "universalien",
                ),
                {5, 54, 55},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "komplex",
                    "komplexität",
                    "komplexitaet",
                    "complexity",
                    "model",
                    "abstraktion",
                ),
                {65, 75, 77},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "2",
                    "zwei",
                    "gerade",
                    "ungerade",
                    "alternierung",
                    "alternierend",
                    "zweierstruktur",
                ),
                {78, 79, 80},
            ),
            (
                Program.ParametersMain.universum,
                ("4", "vier", "viererstruktur", "viererabfolgen"),
                {76, 77, 81},
            ),
            (
                Program.ParametersMain.universum,
                (),
                {5, 54, 55, 65, 75, 76, 77, 78, 79, 80, 81},
            ),
            (
                Program.ParametersMain.wirtschaft,
                ("system",),
                {
                    69,
                },
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "realistisch",
                    "funktioniert",
                ),
                {70},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "erklärung",
                    "erklaerung",
                ),
                {71},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "incel",
                    "incels",
                ),
                {68},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "irrationalezahlendurchwurzelbildung",
                    "ausgangslage",
                ),
                {73},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "dominierendesgeschlecht",
                    "maennlich",
                    "männlich",
                    "weiblich",
                ),
                {51},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "liebe",
                    "ethik",
                ),
                {8, 9, 28},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "glauben",
                    "erkenntnis",
                    "glaube",
                ),
                {59},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "angreifbar",
                    "angreifbarkeit",
                ),
                {58, 57},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "motive",
                    "motivation",
                    "motiv",
                ),
                {10, 18, 42},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "errungenschaften",
                    "ziele",
                    "erhalten",
                ),
                {11},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "erwerben",
                    "erlernen",
                    "lernen",
                    "evolutionaer",
                    "evolutionär",
                    "intelligenz",
                    "kreativität",
                    "kreativitaet",
                    "kreativ",
                ),
                {12, 47, 27, 13, 32},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "brauchen",
                    "benoetigen",
                    "benötigen",
                    "notwendig",
                ),
                {13, 14},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "krankheit",
                    "krankheiten",
                    "pathologisch",
                    "pathologie",
                    "psychiatrisch",
                ),
                {24},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "alpha",
                    "beta",
                    "omega",
                    "sigma",
                ),
                {46},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "anfuehrer",
                    "chef",
                ),
                {29},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "beruf",
                    "berufe",
                ),
                {30},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "loesungen",
                    "loesung",
                    "lösungen",
                    "lösungen",
                ),
                {31},
            ),
            (Program.ParametersMain.menschliches, ("musik",), {33}),
            (
                Program.ParametersMain.procontra,
                (
                    "pro",
                    "dafür",
                    "dafuer",
                ),
                {17, 48},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "contra",
                    "dagegen",
                ),
                {15, 26},
            ),
            (Program.ParametersMain.licht, (), {20, 27}),
            (
                Program.ParametersMain.bedeutung,
                (
                    "primzahlen",
                    "vielfache",
                    "vielfacher",
                ),
                {19},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "anwendungdersonnen",
                    "anwendungenfuermonde",
                ),
                {22},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "zaehlung",
                    "zaehlungen",
                    "zählungen",
                    "zählung",
                ),
                {25, 45},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "jura",
                    "gesetzeslehre",
                    "recht",
                ),
                {34},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "vollkommenheit",
                    "geist",
                ),
                {35},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "gestirn",
                    "mond",
                    "sonne",
                    "planet",
                ),
                {64},
                set(),
                set(),
                set(),
                [
                    True,
                ],
            ),
            (Program.ParametersMain.symbole, (), {36, 37}),
            (
                Program.ParametersMain.primzahlvielfachesuniversum,
                allowedPrimNumbersForCommand,
                set(),
                set(),
                (
                    lambda paraValues: {
                        abs(int(chosen))
                        if chosen.isdecimal() and primCreativity(abs(int(chosen))) == 1
                        else None
                        for chosen in [value for value in (paraValues.split(","))]
                    }
                    - {None, 0, 1},
                ),
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "weisheit",
                    "metaweisheit",
                    "meta-weisheit",
                    "idiot",
                    "weise",
                    "optimal",
                    "optimum",
                ),
                set(),
                {(40, 41)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "gut",
                    "böse",
                    "boese",
                    "lieb",
                    "schlecht",
                ),
                {52, 53},
                {(38, 39)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "zeit",
                    "raum",
                    "zeitlich",
                    "räumlich",
                ),
                set(),
                {(49, 50)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "meinungen",
                    "anderemenschen",
                    "ruf",
                ),
                set(),
                {(60, 61)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "selbstgerechtigkeit",
                    "selbstgerecht",
                ),
                set(),
                {(62, 63)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "egoismus",
                    "altruismus",
                    "egoist",
                    "altruist",
                ),
                set(),
                {(66, 67)},
            ),
            (Program.ParametersMain.inkrementieren, ("universum",), {43, 54, 74}),
            # (
            #     Program.ParametersMain.alles,
            #     (),
            #     set(range(82))
            #     - {67, 66, 63, 62, 61, 60, 56, 44, 49, 50, 41, 40, 39, 38},
            #     {
            #         (40, 41),
            #         (38, 39),
            #         (49, 50),
            #         (60, 61),
            #         (62, 63),
            #         (66, 67),
            #     },
            #     {
            #         couldBePrimeNumber
            #         if primCreativity(couldBePrimeNumber) == 1
            #         else None
            #         for couldBePrimeNumber in range(2, 100)
            #     }
            #     - {
            #         None,
            #     },
            #     set(range(10)),
            # ),
        ]

        Program.kombiParaNdataMatrix = {
            1: (
                "tiere",
                "tier",
                "lebewesen",
            ),
            2: ("berufe", "beruf"),
            3: (
                "kreativität",
                "intelligenz",
                "kreativitaet",
            ),
            4: ("liebe",),
            5: (
                "transzendenz",
                "transzendentalien",
                "strukturalien",
                "alien",
            ),
            6: ("leibnitz", "primzahlkreuz"),
            7: (
                "männer",
                "maenner",
                "frauen",
            ),
            8: (
                "evolution",
                "erwerben",
                "persoenlichkeit",
                "persönlichkeit",
            ),
            9: (
                "religion",
                "religionen",
            ),
        }

        self.kombiReverseDict: dict = {}
        for key, value in Program.kombiParaNdataMatrix.items():
            for valuesInValuess in value:
                self.kombiReverseDict[valuesInValuess] = key

        allValues = [set(), set(), set(), set(), []]
        for possibleCommands in paraNdataMatrix:
            for commandValue, aAllValue in zip(possibleCommands[2:], allValues[:3]):
                try:
                    aAllValue |= commandValue
                except TypeError:
                    alxp(type(commandValue))
                    alxp(commandValue)

        """
        Folgende Schleife ist eigentlich unnötig.
        Sie ist für bool Werte da, wenn Sachen generiert werden.
        Ich brauche aber gerade den bool wert gar nicht mehr, weil es in
        diesem Fall auch anders geht, aber für die Zukunft kann das hilfreich sein.
        Also lasse ich es mal stehen!
        """
        for possibleCommands in paraNdataMatrix:
            for commandValue, aAllValue in zip(possibleCommands[6:], allValues[4:]):
                aAllValue += [commandValue]
        # allValues[1] = allValues[2]
        allValues[2] = set((int(pNum) for pNum in allowedPrimNumbersForCommand))
        allValues[3] = set(Program.kombiParaNdataMatrix.keys())

        paraNdataMatrix += [
            (
                (Program.ParametersMain.alles,),
                (),
                *allValues,
            )
        ]
        # return paraDict1, dataDict1
        """
        Hier wird erreicht, dass beide Dictionaries stückweise aufgefüllt werden.
        Aus den 3 voran gegangen Datenstrukturen werden 2 Dicts gemacht.
        """
        self.paraMainDict, self.paraDict = {}, {}
        for parameterEntry in paraNdataMatrix:
            self.paraDict, self.dataDict = mergeParameterDicts(
                self.paraMainDict,
                self.paraDict,
                self.dataDict,
                *intoParameterDatatype(
                    parameterEntry[0],
                    parameterEntry[1],
                    tuple(
                        parameterEntryElement
                        for parameterEntryElement in parameterEntry[2:]
                    ),
                )
            )
            # alxp("C")
            # alxp(self.dataDict[0])
        self.dataDict[3] = Program.kombiParaNdataMatrix
        alxp("--")
        alxp(self.dataDict)
        alxp("--")
        self.tables.dataDict = self.dataDict

    def parametersToCommandsAndNumbers(
        self, argv, neg=""
    ) -> Iterable[Union[set, set, set, list]]:
        """Parameter in der Shell werden hier vorverarbeitet.
        Die Paraemter führen dazu, dass Variablen gesetzt werden, z.B.
        eine Menge die als Befehl kodiert, welche Zeilen und eine die kodiert
        welche Spaltennummer ausgegeben werden sollen.
        Außerdem welche extra Tabellen geladen werden sollen.

        return paramLines, rowsAsNumbers, rowsOfcombi

        @type  argv: list
        @param argv: Programmparamenter
        @type  neg: str
        @param neg: MinusZeichen davor ?
        @rtype: set, set, set
        @return: Zeilen, Spalten, Spalten anderer Tabellen
        """
        global infoLog, shellRowsAmount  # , puniverseprims
        if len(argv) == 1 and neg == "":
            cliout("Versuche Parameter -h")
        spaltenreihenfolgeundnurdiese: list = []
        puniverseprims_only: set = set()
        rowsAsNumbers: set = set()
        paramLines: set = set()
        self.bigParamaeter: list = []
        self.__willBeOverwritten_rowsOfcombi: set = set()
        generRows = set()
        for arg in argv[1:]:
            if len(arg) > 0 and arg[0] == "-":
                if (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "zeilen"
                ):
                    if arg[2:7] == "alles" and len(neg) == 0:
                        paramLines.add("all")
                    elif arg[2:7] == "zeit=":
                        for subpara in arg[7:].split(","):
                            if neg + "=" == subpara:
                                paramLines.add("=")
                            elif neg + "<" == subpara:
                                paramLines.add("<")
                            elif neg + ">" == subpara:
                                paramLines.add(">")
                    elif arg[2:11] == "zaehlung=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[11:], "n", neg
                            )
                        )
                    elif arg[2:15] == "hoehemaximal=":
                        if arg[15:].isdecimal():
                            self.tables.textHeight = abs(int(arg[15:]))
                    elif arg[2:6] == "typ=":
                        for word in arg[6:].split(","):
                            if word == neg + "sonne":
                                paramLines.add("sonne")
                            elif word == neg + "schwarzesonne":
                                paramLines.add("schwarzesonne")
                            elif word == neg + "planet":
                                paramLines.add("planet")
                            elif word == neg + "mond":
                                paramLines.add("mond")
                    elif arg[2 : 2 + len("potenzenvonzahlen=")] == "potenzenvonzahlen=":
                        for word in arg[2 + len("potenzenvonzahlen=") :].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "^")
                    elif arg[2:21] == "vielfachevonzahlen=":
                        for word in arg[21:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "v")
                    elif arg[2:20] == "primzahlvielfache=":
                        for word in arg[20:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "p")
                    elif arg[2:22] == "vorhervonausschnitt=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[22:], "a", neg
                            )
                        )
                    elif arg[2:21] == "nachtraeglichdavon=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[21:], "z", neg
                            )
                        )
                    elif len(neg) > 0:
                        cliout(
                            'Den Neben-Parameter "'
                            + arg
                            + '" gibt es hier nicht für den Hauptparameter "-'
                            + self.bigParamaeter[-1]
                            + '".'
                        )
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "ausgabe"
                ):  # unteres Kommando
                    if (
                        arg[2 : 2 + len("spaltenreihenfolgeundnurdiese=")]
                        == "spaltenreihenfolgeundnurdiese="
                    ):
                        for number in arg[
                            2 + len("spaltenreihenfolgeundnurdiese=") :
                        ].split(","):
                            if str(number).isdecimal():
                                spaltenreihenfolgeundnurdiese += [int(number)]
                    elif arg[2:6] == "art=":
                        outputtype = arg[(arg.find("=") + 1) :]
                        if outputtype == "shell":
                            self.tables.outType = OutputSyntax()
                        elif outputtype == "csv":
                            self.tables.outType = csvSyntax()
                        elif outputtype == "bbcode":
                            self.htmlOrBBcode = True
                            self.tables.outType = bbCodeSyntax()
                        elif outputtype == "html":
                            self.tables.outType = htmlSyntax()
                            self.htmlOrBBcode = True
                        elif outputtype == "markdown":
                            self.tables.outType = markdownSyntax()
                    elif arg[2:] in ["nocolor", "justtext"] and neg == "":
                        self.tables.getOut.color = False
                    elif (
                        arg[2:] in ["endlessscreen", "endless", "dontwrap", "onetable"]
                        and neg == ""
                    ):
                        self.tables.getOut.oneTable = True
                    elif len(neg) == 0:
                        cliout(
                            'Den Neben-Parameter "'
                            + arg
                            + '" gibt es hier nicht für den Hauptparameter "-'
                            + self.bigParamaeter[-1]
                            + '".'
                        )
                else:  # oberes Kommando
                    if arg[1:] in ["zeilen", "spalten", "kombination", "ausgabe"]:
                        self.bigParamaeter += [arg[1:]]
                    elif arg[1:] in ["debug"]:
                        infoLog = True
                    elif arg[1:] in ["h", "help"] and neg == "":
                        self.helpPage()
        if not self.tables.getOut.oneTable:
            self.tables.textWidth = (
                self.tables.textWidth
                if shellRowsAmount > self.tables.textWidth + 8 or shellRowsAmount <= 0
                else shellRowsAmount - 8
            )
        return (
            paramLines,
            rowsAsNumbers,
            self.__willBeOverwritten_rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            puniverseprims_only,
            generRows,
        )

    def helpPage(self):
        global folder
        if "Brython" not in sys.version.split():
            place = os.path.join(
                os.getcwd(), os.path.dirname(__file__), os.path.basename("./readme.txt")
            )
        else:
            place = "readme.txt"
        with open(place) as f:
            read_data = f.read()
        parser.REPLACE_COSMETIC = ()
        html = parser.format(read_data, replace_cosmetic=False)
        if "Brython" not in sys.version.split():
            h = html2text.HTML2Text()
            h.style = "compact"
            plaintext = h.handle(html)
            plaintext = re.sub(r"\\--", "--", plaintext)
            plaintext = re.sub(r"(\*\s+[^\-])", r"\t\1", plaintext)
            plaintext = re.sub(r" \*\*", r"", plaintext)
            plaintext = re.sub(r"\*\s\*", r"", plaintext)
            plaintext = re.sub(r"(\n)([^\s])", r"\1\t\t\2", plaintext)
            plaintext = re.sub(r".*(\* -spalten)", r" \1", plaintext)
            cliout(plaintext)
        else:
            print(html)

    def bringAllImportantBeginThings(self, argv) -> tuple:
        """Einlesen der ersten Tabelle "religion.csv" zu self.relitable
        aller anderen csv dateien
        Parameter werden in Befehle und Nummernlisten gewandelt
        csv Dateien werden angehangen an self.relitable


        @rtype: tuple(int,set,set,list,set,list,set,list,list)
        @return: Spaltenanzahl, Zeilen Ja, Zeilen Nein, Religionstabelle, Spalten, weitere Tabelle daneben, spalten weitere Tabelle, weitere Tabelle für wie sql-join, deren spalten
        """
        global folder, shellRowsAmount
        if "Brython" not in sys.version.split():
            place = os.path.join(
                os.getcwd(),
                os.path.dirname(__file__),
                os.path.basename("./religion.csv"),
            )
        else:
            place = "religion.csv"
        with open(place, mode="r") as csv_file:
            self.relitable: list = []
            for i, col in enumerate(csv.reader(csv_file, delimiter=";")):
                self.relitable += [col]
                if i == 0:
                    self.RowsLen = len(col)
        self.htmlOrBBcode = False
        self.breiteORbreiten = False
        (
            paramLines,
            self.rowsAsNumbers,
            self.rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            self.puniverseprims,
            self.generRows,
        ) = self.parametersToCommandsAndNumbers(argv)
        (
            paramLinesNot,
            self.rowsAsNumbersNot,
            self.rowsOfcombiNot,
            spaltenreihenfolgeundnurdieseNot,
            self.puniverseprimsNot,
            self.generRowsNot,
        ) = self.parametersToCommandsAndNumbers(argv, "-")
        self.dataDict: tuple = [{}, {}, {}, {}]
        self.spaltenTypeNaming: namedtuple = namedtuple(
            "SpaltenTyp",
            "ordinary generated1 concat1 kombi1 bool1 ordinaryNot generate1dNot concat1Not kombi1Not bool1Not",
        )
        self.spaltenTypeNaming = self.spaltenTypeNaming(
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
        )

        # self.spaltenArtenNameKey_SpaltenArtenTupleVal_4Key4otherDict = {
        #    "ordinary": (0, 0),
        #    "generated1": (0, 1),
        #    "concat1": (0, 2),
        #    "kombi1": (0, 3),
        #    "ordinaryNot": (1, 0),
        #    "generate1dNot": (1, 1),
        #    "concat1Not": (1, 2),
        #    "kombi1Not": (1, 3),
        # }
        self.spaltenArtenKey_SpaltennummernValue = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (0, 3): set(),
            (0, 4): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (1, 3): set(),
            (1, 4): set(),
        }
        self.storeParamtersForColumns()
        self.produceAllSpaltenNumbers()
        if self.htmlOrBBcode and not self.breiteORbreiten:
            shellRowsAmount = 0
            self.tables.textWidth = 0

        paramLines, paramLinesNot = self.tables.getPrepare.deleteDoublesInSets(
            paramLines, paramLinesNot
        )
        self.rowsAsNumbers = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.ordinary
        ]
        self.generRows = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.generated1
        ]
        self.puniverseprims = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.concat1
        ]
        self.rowsOfcombi = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.kombi1
        ]
        for prims in self.puniverseprims:
            self.tables.primUniversePrimsSet.add(prims)

        if len(self.rowsOfcombi) > 0:
            paramLines.add("ka")
        self.tables.generRows = self.generRows
        self.tables.getPrepare.rowsAsNumbers = self.rowsAsNumbers
        self.tables.getOut.rowsAsNumbers = self.rowsAsNumbers
        self.relitable, rowsAsNumbers = self.tables.getConcat.readConcatCsv(
            self.relitable, self.rowsAsNumbers
        )
        self.relitable, self.rowsAsNumbers = self.tables.getConcat.concatRowsOfConcepts(
            self.relitable, self.tables.generRows, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatPrimCreativityType(
            self.relitable, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatMondExponzierenLogarithmusTyp(
            self.relitable, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concat1RowPrimUniverse2(
            self.relitable, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatLovePolygon(self.relitable, self.rowsAsNumbers)

        if len(self.rowsOfcombi) > 0:
            (
                animalsProfessionsTable,
                self.relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            ) = self.tables.getCombis.readKombiCsv(
                self.relitable, self.rowsAsNumbers, self.rowsOfcombi
            )
        else:
            animalsProfessionsTable = []
            kombiTable_Kombis = []
            maintable2subtable_Relation = []
        return (
            self.RowsLen,
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
            animalsProfessionsTable,
            self.rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
            spaltenreihenfolgeundnurdiese,
        )

    def __init__(self, argv=[]):
        global Tables, infoLog
        self.argv = argv
        self.allesParameters = 0
        self.tables = Tables()
        self.workflowEverything(argv)

    def workflowEverything(self, argv):
        global infoLog
        (
            self.RowsLen,
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
            animalsProfessionsTable,
            self.rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
            spaltenreihenfolgeundnurdiese,
        ) = self.bringAllImportantBeginThings(argv)
        self.tables.getMainTable.createSpalteGestirn(self.relitable, self.rowsAsNumbers)
        (
            finallyDisplayLines,
            newTable,
            numlen,
            rowsRange,
            old2newTable,
        ) = self.tables.getPrepare.prepare4out(
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
        )
        if len(self.rowsOfcombi) > 0:
            newTable = self.combiTableWorkflow(
                animalsProfessionsTable,
                finallyDisplayLines,
                kombiTable_Kombis,
                maintable2subtable_Relation,
                newTable,
                old2newTable,
                paramLines,
            )
        # rowAmounts = self.tables.getOut.oneTableToMany(newTable, True, rowsRange)
        # spaltenreihenfolgeundnurdiese
        newTable = self.tables.getOut.onlyThatColumns(
            newTable, spaltenreihenfolgeundnurdiese
        )
        self.tables.getOut.cliOut(finallyDisplayLines, newTable, numlen, rowsRange)
        alxp(
            "1. http://goexchange.de/viewtopic.php?f=13&t=2683#p17239 () \n    9. anderen etwas vormachen können (Bahai)\n    1/9. den anderen Strukturgrößen außer der Einheit (9, 1/9) etwas vormachen können"
        )
        alxp(
            """Die Modallogikvielfacher müsste ich noch einprogrammieren
             Wenn ich programmiert habe, wie multipliziert wird, um zu erreichen, dass die Modallogiken umgesetzt werden, werde ich
             programmieren, dass die bisherige Multiplikation, die man kaum verstehen kann, auch besser verständlich gemacht werden kann und sich ggf.
             auf 2 Spalten oder mehr erstrecken wird, statt auf einer, wie bisher. So wird es verständlicher"""
        )
        alxp("""Die Sachen "obwohl man nicht kann" aus Symboliken nehmen.""")
        alxp(
            """ Spalte und Programmierung zu Basis zu Irrationalen Zahlen fehlt vom Thema Symboliken auf Seite 23 """
        )
        alxp("vim: iIaAoOjJ mit Registern arbeiten wegen Löschen ohne ausschneiden")
        alxp(
            """Ich könnte einen schnelleren String oder Listen usw. Datentyp erschaffen.
             Dazu erbe ich String oder etc. den Addieren oder so Operator schreibe ich um.
             dass der sich die Stellen nur merken soll und nicht konkatenieren soll.
             Dann gibt es dann am Ende nur noch so einen Extra-Befehl, der das dann erst wirklich konkatenieren soll!
            Mit f-string concateniert er am Schnellsten, gut ist auch: building a list of strings, then calling "".join()
            plus damit zusammen:  using a list comprehension inline
            """
        )
        alxp(
            """ Überlegen wo ich besser Hashmaps statt Listen verwenden sollte oder Tuple"""
        )
        alxp("Die meisten Listen durch Dicts ersetzen: fast immer schneller! ")
        alxp(
            "Die Geschwindigkeitsteigerugnen entstehn meist durch anschließndes Zusammenfügen zu einer dann festen Größe."
        )
        # alxp("1. Clean Code\n2. Vollständigkeit der Befehle auch")

    def combiTableWorkflow(
        self,
        animalsProfessionsTable,
        finallyDisplayLines,
        kombiTable_Kombis,
        maintable2subtable_Relation,
        newTable,
        old2newTable,
        paramLines,
    ):
        """alle  Schritte für kombi:
        1. lesen: KombiTable und relation, was von kombitable zu haupt gehört
                  und matrix mit zellen sind zahlen der kombinationen
                  d.h. 3 Sachen sind das Ergebnis
        2. prepare: die Zeilen, die infrage kommen für Kombi, d.h.:
                                key = haupttabellenzeilennummer
                                value = kombitabellenzeilennummer
        3. Zeilenumbruch machen, wie es bei der Haupt+Anzeige-Tabelle auch gemacht wurde
           prepare4out
        4. Vorbereiten des Joinens beider Tabellen direkt hier rein programmiert
           (Müsste ich unbedingt mal refactoren!)
        5. joinen
           Wenn ich hier jetzt alles joine, und aber nicht mehrere Zellen mache pro Kombitablezeile,
           d.h. nicht genauso viele Zeilen wie es der Kombitablezeilen entspricht,
           d.h. ich mache nur eine Zeile, in der ich alle kombitableteilen nur konkatteniere,
           dann ist das Ergebnis Mist in der Ausagbe, weil der Zeilenumbruch noch mal gemacht werden müsste,
           der jedoch bereits schon gemacht wurde.
           Der musste aber vorher gemacht werden, denn wenn man ihn jetzt machen würde,
           dann müsste man das eigentlich WIEDER mit der ganzen Tabelle tun!
           Also etwa alles völlig umprogrammieren?
        6. noch mal nur das ausgeben lassen, das nur ausgegeben werden soll
        7. letztendliche Ausagebe von allem!!
        """
        ChosenKombiLines = self.tables.getCombis.prepare_kombi(
            finallyDisplayLines,
            animalsProfessionsTable,
            paramLines,
            finallyDisplayLines,
            kombiTable_Kombis,
        )
        (
            finallyDisplayLines_kombi,
            newTable_kombi_1,
            lineLen_kombi_1,
            animalsProfessionsTable,
            old2newTableAnimalsProfessions,
        ) = self.tables.getPrepare.prepare4out(
            set(),
            set(),
            animalsProfessionsTable,
            self.rowsOfcombi,
            self.tables.getCombis.sumOfAllCombiRowsAmount,
        )
        KombiTables = self.tables.getCombis.prepareTableJoin(
            ChosenKombiLines, newTable_kombi_1
        )
        newTable = self.tables.getCombis.tableJoin(
            newTable,
            KombiTables,
            maintable2subtable_Relation,
            old2newTable,
            self.rowsOfcombi,
        )
        return newTable


if __name__ == "__main__":
    Program(sys.argv)

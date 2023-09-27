#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../libs"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import reta
import LibRetaPrompt

# LibRetaPrompt.spaltenDict = {"konzept": ["Selbstlosigkeit_Ichlosigkeit_etc"]}

zeile: int = 10
beginVonVorn = False
merke = []


def onExit():
    global merke
    print("gemerkt:")
    for merk in merke:
        print(merk)


def printResult(table: list, befehl: list):
    global merke
    table2: list = []
    tableGestreift: list = []
    for line in table:
        if len(line.strip()) > 0:
            table2 += [line]
            tableGestreift += [line.split()]

    # print("len:")
    # print(len(table2))
    ifExit = False
    if len(table2) <= 1:
        merke += ["leer1, exit"]
        ifExit = True
    if not any((t[0].strip() == str(zeile) for t in tableGestreift)):
        merke += ["leer2, exit"]
        ifExit = True
    # if ifExit:
    #    onExit()


weiter = beginVonVorn
gabEsSchonMal: set = set()

# alleSpaltenParamter: dict = {
#    tuple(value): key for key, value in LibRetaPrompt.spaltenDict.items()
# }
# alleSpaltenParamter = {value: key for key, value in alleSpaltenParamter.items()}
try:
    alleSpaltenParamter = LibRetaPrompt.spaltenDict
    for spaltenOberkategorie, spaltenListe in alleSpaltenParamter.items():
        import reta
        import LibRetaPrompt

        befehle = []
        if len(spaltenListe) == 0:
            if weiter:
                befehle += [
                    [
                        "reta",
                        "-zeilen",
                        "--vorhervonausschnitt=" + str(zeile),
                        "-spalten",
                        "--" + spaltenOberkategorie,
                        "-ausgabe",
                        "--breite=0",
                        "--onetable",
                    ]
                ]
        else:
            for einigeSpalten in spaltenListe:
                if not weiter and not beginVonVorn:
                    if (
                        len({"Grundstrukturen"} & {spaltenOberkategorie}) > 0
                        and len({"universellerkomperativ"} & {einigeSpalten}) > 0
                    ):
                        weiter = True
                        print(spaltenListe)
                lenA = len(gabEsSchonMal)
                gabEsSchonMal |= {einigeSpalten}
                lenB = len(gabEsSchonMal)
                if weiter and lenA != lenB:
                    befehle += [
                        [
                            "reta",
                            "-zeilen",
                            "--vorhervonausschnitt=" + str(zeile),
                            "-spalten",
                            "".join(("--", spaltenOberkategorie, "=", einigeSpalten)),
                            "-ausgabe",
                            "--breite=0",
                            "--onetable",
                        ]
                    ]
                    for befehl in befehle:
                        print(" ".join(befehl))
                        prog = reta.Program(befehl)
                        printResult(prog.resultingTable, befehl)
except KeyboardInterrupt:
    onExit()

#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../libs"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from center import i18n
import reta

# LibRetaPrompt.spaltenDict = {"konzept": ["Selbstlosigkeit_Ichlosigkeit_etc"]}

zeile: int = 10
beginVonVorn = True
merke: list = []


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
        merke += [" ".join(["leer1"] + befehl)]
        ifExit = True
    if not any((t[0].strip() == str(zeile) for t in tableGestreift)):
        merke += [" ".join(["leer2"] + befehl)]
        ifExit = True
    if ifExit:
        onExit()


weiter = beginVonVorn
gabEsSchonMal: set = set()

# prog: reta.Program = reta.Program(["reta", "-nichts"])
# alleSpaltenParamter: dict = {
#    tuple(value): key for key, value in LibRetaPrompt.spaltenDict.items()
# }
# alleSpaltenParamter = {value: key for key, value in alleSpaltenParamter.items()}
prog: reta.Program = reta.Program([sys.argv[0], "-" + i18n.retapy.nichtsWort])
spaltenDict: dict = {}
for tupel in prog.paraNdataMatrix:
    try:
        tupel[3]
        nebenNebenPara = (
            # tuple(tupel[1])
            tuple(tupel[1])[0]
            if all(val.isnumeric for val in tupel[1])
            else tupel[1][0]
        )
        if nebenNebenPara != "alles":
            try:
                spaltenDict[tupel[0][0]] += [nebenNebenPara]
            except KeyError:
                spaltenDict[tupel[0][0]] = [nebenNebenPara]
    except IndexError:
        pass

try:
    # alleSpaltenParamter = LibRetaPrompt.spaltenDict
    alleSpaltenParamter = spaltenDict
    for spaltenOberkategorie, spaltenListe in alleSpaltenParamter.items():
        befehle = []
        if False and len(spaltenListe) == 0:
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
                # einigeSpalten = spaltenListe
                # if not weiter and not beginVonVorn:
                # if (
                #    len({"Grundstrukturen"} & {spaltenOberkategorie}) > 0
                #    and len({"filter"} & {einigeSpalten}) > 0
                # ):
                #    weiter = True
                #    print(spaltenListe)
                # lenA = len(gabEsSchonMal)
                # gabEsSchonMal |= {einigeSpalten}
                # lenB = len(gabEsSchonMal)
                # if weiter and lenA != lenB:
                # if weiter:
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
                # for befehl in befehle:
                befehl = befehle[-1]
                print(" ".join(befehl))
                del prog
                prog = reta.Program(befehl)
                printResult(prog.resultingTable, befehl)
except KeyboardInterrupt:
    onExit()
onExit()

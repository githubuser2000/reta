#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../libs"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import reta
import LibRetaPrompt

LibRetaPrompt.spaltenDict = {"konzept": ["Selbstlosigkeit_Ichlosigkeit_etc"]}

zeile: int = 10


def printResult(table: list):
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
        print("leer1, exit")
        ifExit = True
    if not any((t[0].strip() == str(zeile) for t in tableGestreift)):
        print("leer2, exit")
        ifExit = True
    if ifExit:
        exit()


for spaltenOberkategorie, spaltenListe in LibRetaPrompt.spaltenDict.items():
    if len(spaltenListe) == 0:
        prog = reta.Program(
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
        )
        printResult(prog.resultingTable)
    else:
        for einigeSpalten in spaltenListe:
            prog = reta.Program(
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
            )
            printResult(prog.resultingTable)

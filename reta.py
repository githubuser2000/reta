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
                           primzahlvielfachesgalaxie, re, shellRowsAmount, sys,
                           x)

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

        def resultingSpaltenFromTuple(
            tupl: tuple, neg, paraValue=None, befehlName=None
        ) -> tuple:
            # x("SDH1", [befehlName in Program.ParametersMain.primvielfache, paraValue])
            for i, eineSpaltenArtmitSpaltenNummern in enumerate(tupl):
                """
                Die Variable self.tables.spalteGestirn braucht man gar nicht mehr !!!
                """
                if (
                    type(eineSpaltenArtmitSpaltenNummern) in [list, tuple]
                    and len(eineSpaltenArtmitSpaltenNummern) > 0
                ):
                    # alxp("1")
                    if type(eineSpaltenArtmitSpaltenNummern[0]) is bool:
                        # alxp("2")
                        eineSpaltenArtmitSpaltenNummern = set(
                            eineSpaltenArtmitSpaltenNummern
                        )
                    elif type(eineSpaltenArtmitSpaltenNummern[0]) in [tuple, list]:
                        # alxp("3")
                        eineSpaltenArtmitSpaltenNummern = set(
                            eineSpaltenArtmitSpaltenNummern[0]
                        )
                if i == 2 and (
                    type(eineSpaltenArtmitSpaltenNummern)
                    in [
                        list,
                        tuple,
                        # set,
                    ]
                    or befehlName in Program.ParametersMain.gebrochenuniversum[0]
                    or befehlName in Program.ParametersMain.gebrochengalaxie[0]
                ):
                    # alxp("4")
                    if (
                        befehlName
                        == Program.ParametersMain.primzahlvielfachesgalaxie[0]
                    ):
                        # alxp("5")
                        self.spaltenArtenKey_SpaltennummernValue[
                            (len(neg), 2)
                        ] |= Program.lambdaPrimGalax(paraValue)
                    elif befehlName in Program.ParametersMain.gebrochenuniversum[0]:
                        # alxp("N6N")
                        self.spaltenArtenKey_SpaltennummernValue[
                            (len(neg), 5)
                        ] |= Program.lambdaGebrUnivUndGalax(paraValue)
                    elif befehlName in Program.ParametersMain.gebrochengalaxie[0]:
                        # alxp("N8N")
                        self.spaltenArtenKey_SpaltennummernValue[
                            (len(neg), 6)
                        ] |= Program.lambdaGebrUnivUndGalax(paraValue)
                        # alxp("N9N")
                    else:
                        print(befehlName)
                        raise ValueError
                elif (
                    paraValue == "beschrieben"
                    and befehlName in Program.ParametersMain.primvielfache
                ):
                    self.spaltenArtenKey_SpaltennummernValue[(len(neg), 2)] |= {2}
                else:
                    try:
                        # alxp("N11N")
                        self.spaltenArtenKey_SpaltennummernValue[
                            (len(neg), i)
                        ] |= eineSpaltenArtmitSpaltenNummern
                        # alxp("N12N")
                    except TypeError:
                        pass
            # alxp("N10N")
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
                ] -= self.spaltenArtenKey_SpaltennummernValue.pop((1, el2Type))

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
            if len(cmd) > 1 and cmd[0] == "-" and cmd[1] != "-":
                if cmd[1:] in mainParaCmds.keys():
                    lastMainCmd = mainParaCmds[cmd[1:]]
                elif len(neg) == 0:
                    # else:
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
                            elif shellRowsAmount > 6 and breite > shellRowsAmount - 6:
                                breite = shellRowsAmount - 6
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
                                    resultingSpaltenFromTuple(
                                        self.paraDict[
                                            (cmd[:eq], oneOfThingsAfterEqSign)
                                        ],
                                        neg,
                                        oneOfThingsAfterEqSign,
                                        befehlName=cmd[:eq],
                                    )
                                    # x("DFGH", self.spaltenArtenKey_SpaltennummernValue)
                                except KeyError:
                                    nebenParameters: list = []
                                    nebenparameterWerte: list = []
                                    for value in self.paraDict.keys():
                                        nebenParameters += [value[0]]
                                        nebenparameterWerte += [value[1]]

                                    if cmd[:eq] in nebenParameters:
                                        possibleNebenparameterWert: list = []
                                        for nebenParameter, nebenparameterWert in zip(
                                            nebenParameters,
                                            nebenparameterWerte,
                                        ):
                                            if nebenParameter == cmd[:eq]:
                                                possibleNebenparameterWert += [
                                                    nebenparameterWert
                                                ]

                                        cliout(
                                            'Der Unter-Paramaeter "--'
                                            + cmd[:eq]
                                            + '" existiert, aber nicht mit dem Textwert "'
                                            + oneOfThingsAfterEqSign
                                            + '" mögliche Nebenparameter-Textwerte, für diesen Unter-Parameter, sind: '
                                            + ",".join(possibleNebenparameterWert)
                                        )
                                    else:
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

                                resultingSpaltenFromTuple(
                                    self.paraDict[(cmd, "")], neg, befehlName=cmd
                                )

                        except KeyError:
                            cliout(
                                'Der Unter-Parameter "--'
                                + cmd
                                + '" existiert hier nicht als Befehl für Haupt-Parameter'
                                + " -spalten"
                                + ", oder dieser Parameter braucht Werte analog wie: \n--unterParameter=Wert1\n"
                                + "Es ist nur möglich: --"
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
                                        befehlName="kombinationen",
                                    )
                                    # alxp("geht 2:")
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
            """
            ALLE PARAMETER DIESER FUNKTION SIND EIGENTLICH NUR EIN JEWEILIGES ELEMENT VON
            paraNdataMatrix
            ZUSAMMEN

            Speichert einen Parameter mit seinem DatenSet
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
            dataDicts: tuple = ({}, {}, {}, {}, {}, {}, {}, {})

            # datas sind nicht die Haupt-und-Neben-Parameter, sondern alles das diese enthalten und meinen können
            # ein datas Datensatz sind alle sets, die ein Haupt-Neben-Parameter Zusammenhang enthalten kann an sets
            for i, d in enumerate(datas):
                for spaltenNummerOderEtc in d:
                    # spaltenNummerOderEtc ist hier also eine Zahl von einem set, die z.B. eine Spaltennummer meinen kann
                    into = []
                    parameterMainNamePerLoop = []
                    case: int = None

                    # das mit 2 Schleifen nur deshalb, damit immer alle Haupt- und Neben-Parameter in die Liste rein kommen
                    for parameterMainName in parameterMainNames:
                        for parameterName in (
                            parameterNames if len(parameterNames) > 0 else ("",)
                        ):
                            # i ist die Nummer welches Set es ist
                            if i == 4 and (
                                type(spaltenNummerOderEtc) is bool
                                or (
                                    type(spaltenNummerOderEtc) in [tuple, list]
                                    and len(spaltenNummerOderEtc) > 0
                                    and type(spaltenNummerOderEtc[0]) is bool
                                )
                            ):
                                case = 1
                                into += [
                                    (
                                        parameterMainName,
                                        parameterName,
                                    )
                                ]
                            elif i in (5, 6):  # and type(spaltenNummerOderEtc) is set:
                                # x("SIC", [i, spaltenNummerOderEtc])
                                case = 2
                                into += [[(parameterMainName, parameterName)]]
                                # x("mmm", into)
                                parameterMainNamePerLoop += [parameterName]
                            elif i == 2 and callable(spaltenNummerOderEtc):
                                case = 2
                                parameterMainNamePerLoop += [parameterName]
                                into += [[(parameterMainName, parameterName)]]
                                # x("ooo", into)
                                # x("ert", [parameterName, parameterMainName])
                            elif i == 4 and (
                                type(spaltenNummerOderEtc) in (list, tuple)
                            ):
                                case = 4
                                into += [(parameterMainName, parameterName)]
                            elif i == 4 and (type(spaltenNummerOderEtc) in (set,)):
                                case = 4
                                into += [(parameterMainName, parameterName)]
                                spaltenNummerOderEtc = spaltenNummerOderEtc.pop()
                            # elsif i ==7 and type(spaltenNummerOderEtc) is str:
                            else:
                                case = 3
                                try:
                                    into += [(parameterMainName, parameterName)]
                                except KeyError:
                                    into = [(parameterMainName, parameterName)]

                    # if i == 7:
                    #    x("SDV", d)
                    index1 = i if case != 1 else 3
                    index2a = (
                        spaltenNummerOderEtc
                        if case == 3
                        else (
                            spaltenNummerOderEtc
                            if case == 4
                            else ("bool", 0)
                            if case == 1
                            else tuple(
                                (
                                    int(para)
                                    if para.isdecimal()
                                    else para
                                    if len(parameterNames) > 0
                                    else None
                                    for para in parameterMainNamePerLoop
                                )
                            )
                            if case == 2
                            else None
                        )
                    )
                    intoA = into if case == 2 else (into,)
                    for index2, into2 in zip_longest(
                        index2a if case == 2 else (index2a,), intoA, fillvalue=into
                    ):
                        try:
                            dataDicts[index1][index2] += (
                                (into2,)
                                if dataDicts[index1][index2][-1] != into2
                                else ()
                            )
                        except KeyError:
                            dataDicts[index1][index2] = (into2,)
            # if case == 2:
            # x("dadaDick", dataDicts)
            # x("PARA", paraDict)
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
            beiden Parameter sagen, welche Spalten es alle sind.

            *paraNdataMatrix*
            enthält die meisten Parameternamen mit den zugehörigen Spaltennummern mit Sonderdaten, weil einige Spalten generiert werden aus anderen

            u.a. daraus wird das *paraDict* und *dataDict* gebaut. Beides hat das Gleiche drin, nur das andere jeweils mit Key und Value vertauscht.
            Darin sind die Paramenternamen und csv Spaltennummern drin, die nicht verwechselt werden dürfen mit den dann real vorhandenen Spaltennummern, die nicht die gleichen als Zahl sind, wie die in der CSV-Datei.

            *self.tables.generatedSpaltenParameter*
            key ist Spaltennummer der Ausgabe, value ist ein Paar von 2 Strings über Überparametername und Unterparametername für den Klassenname für die Spalte des HTML-Tags.
            <em>
            Das beinhaltet das für alle Parameter und Ausgabe-Spalten-Nummern.</em>"""

            # x("QARA", (paraMainDict1, paraMainDict2))
            paraMainDict1 = {**paraMainDict1, **paraMainDict2}
            # x("QARA", (paraDict1, paraDict2))
            paraDict1 = {**paraDict1, **paraDict2}
            # x("uofs1", dataDicts1)
            # x("uofs2", dataDicts2)
            dataDicts3 = deepcopy(dataDicts1)
            for i, (dict1, dict2) in enumerate(
                # zip_longest(dataDicts1, dataDicts2, fillvalue=dict())
                zip_longest(dataDicts1, dataDicts2)
            ):
                # if i == 4:
                #    x("qqq", (dict1, dict2))
                if type(dict1) is dict and type(dict2) is dict:
                    if len(dataDicts3[i].keys()) == 0:
                        dataDicts3[i] = dataDicts2[i]
                    else:
                        for key1, value1 in dict1.items():
                            for key2, value2 in dict2.items():
                                if key2 == key1:
                                    # x("DING1", dataDicts3[i][key1])
                                    # x("DING2", value2)
                                    dataDicts3[i][key1] += value2
                                elif key2 not in dataDicts3[i].keys():
                                    # x("DONG", value2)
                                    dataDicts3[i][key2] = value2
                elif type(dict1) is dict and dict2 is None:
                    dataDicts3[i] = dict1
                elif dict1 is None and type(dict2) is dict:
                    # x("234", i)
                    dataDicts3[i] = dict2
            # x("uufs", dataDicts3)
            # alxp(dataDicts3)
            # x("QORA", (paraDict1))
            return paraDict1, dataDicts3

        Program.ParametersMain: namedtuple = namedtuple(
            "ParametersMain",
            "religionen galaxie strukturgroesse universum wirtschaft menschliches procontra licht bedeutung symbole primzahlvielfachesgalaxie konzept inkrementieren operationen universummetakonkret primzahlwirkung gebrochenuniversum gebrochengalaxie primvielfache alles",
        )

        Program.ParametersMain = Program.ParametersMain(
            (
                "Religionen",
                "religionen",
                "religion",
            ),
            (
                "Galaxie",
                "galaxie",
                "alteschriften",
                "kreis",
                "galaxien",
                "kreise",
            ),
            (
                "Größenordnung",
                "groessenordnung",
                "strukturgroesse",
                "strukturgroeße",
                "strukturgrösse",
                "strukturgröße",
                "groesse",
                "stufe",
                "organisationen",
            ),
            (
                "Universum",
                "universum",
                "transzendentalien",
                "strukturalien",
                "kugel",
                "kugeln",
                "ball",
                "baelle",
                "bälle",
            ),
            ("Wirtschaft", "wirtschaft"),
            (
                "Menschliches",
                "menschliches",
            ),
            (
                "Pro_Contra",
                "procontra",
                "dagegendafuer",
            ),
            (
                "Licht",
                "licht",
            ),
            (
                "Bedeutung",
                "bedeutung",
            ),
            (
                "Symbole",
                "symbole",
            ),
            tuple(a[0] for a in primzahlvielfachesgalaxie),
            (
                "Eigenschaften",
                "eigenschaften",
                "eigenschaft",
                "konzept",
                "konzepte",
            ),
            (
                "Inkrementieren",
                "inkrementieren",
            ),
            (
                "Operationen",
                "operationen",
            ),
            (
                "Meta_vs_Konkret_(Universum)",
                "universummetakonkret",
            ),
            (
                "Primzahlwirkung",
                "primzahlwirkung",
            ),
            # ("Gebrochen-Rational_Universum", "gebrochenuniversum"),
            ("gebrochenuniversum",),
            ("gebrochengalaxie",),
            ("Primvielfache", "primvielfache"),
            ("alles",),
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

        Program.lambdaGebrUnivUndGalax = lambda paraValues: {
            abs(int(chosen)) if chosen.isdecimal() else None
            for chosen in [value for value in (paraValues.split(","))]
        } - {None, 0, 1}

        Program.lambdaPrimGalax = lambda paraValues: {
            abs(int(chosen))
            if chosen.isdecimal() and primCreativity(abs(int(chosen))) == 1
            else None
            for chosen in [value for value in (paraValues.split(","))]
        } - {None, 0, 1}

        paraNdataMatrix = [
            (
                Program.ParametersMain.operationen,
                (
                    "Halbierung",
                    "halbierung",
                    "halbierungen",
                ),
                {86},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "Religions-Gründer-Typ",
                    "religionsgründertyp",
                    "prophet",
                    "archon",
                    "religionsgruendertyp",
                ),
                {72},
            ),
            (
                Program.ParametersMain.religionen,
                ("Sternpolygon", "sternpolygon"),
                {0, 6, 36},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "der_Tierkreiszeichen",
                    "dertierkreiszeichen",
                    "babylon",
                ),
                {0, 36},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "Sternpolygon_vs_gleichförmiges",
                    "vergleich",
                    "sternpolygonvsgleichfoermiges",
                    "vergleichnvs1divn",
                ),
                {87},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "Messias",
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
                    "gleichförmiges_Polygon",
                    "gleichförmigespolygon",
                    "gleichfoermigespolygon",
                    "nichtsternpolygon",
                    "polygon",
                ),
                {16, 37},
            ),
            (
                Program.ParametersMain.religionen,
                (
                    "Vertreter_höherer_Konzepte",
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
                    "Offenbarung_des_Johannes",
                    "offenbarung",
                    "offenbarungdesjohannes",
                    "johannes",
                    "bibel",
                    "offenbarungjohannes",
                ),
                {90},
            ),
            (
                Program.ParametersMain.universum,
                ("keine_Nur-Paradigma-Religionen", "metaparadigmareligion"),
                {190, 191, 196},
            ),
            (
                Program.ParametersMain.universum,
                ("Kugeln_Kreise", "kugelnkreise", "kugeln", "kreise"),
                {77, 145},
            ),
            (
                Program.ParametersMain.galaxie,
                ("Kugeln_Kreise", "kugelnkreise", "kugeln", "kreise"),
                {77, 145},
            ),
            (
                Program.ParametersMain.galaxie,
                ("chinesisches_Horoskop", "chinesischeshoroskop", "china"),
                {91},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "babylonische_Tierkreiszeichen",
                    "tierkreiszeichen",
                    "babylon",
                ),
                {1, 2},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "Thomasevangelium",
                    "thomasevangelium",
                    "thomas",
                ),
                {0, 3},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "analytische_Ontologie",
                    "analytischeontologie",
                    "ontologie",
                ),
                {84},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "Transzendentalien_innen_außen",
                    "innenaussenstrukur",
                    "strukturalieninnenaußen",
                    "strukturalieninnenaussen",
                    "innenaußenstrukur",
                    "transzendentalieninnenaußen",
                    "transzendentalieninnenaussen",
                ),
                {149},
            ),
            (
                Program.ParametersMain.galaxie,
                (
                    "Modallogik",
                    "modallogik",
                ),
                {148},
            ),
            (
                Program.ParametersMain.operationen,
                (
                    "5",
                    "fünf",
                    "fünfer",
                    "fünferstruktur",
                    "fuenf",
                    "fuenfer",
                    "fuenferstruktur",
                ),
                {96},
            ),
            (
                Program.ParametersMain.operationen,
                (
                    "9",
                    "neun",
                    "neuner",
                    "neunerstruktur",
                ),
                {94},
            ),
            (
                Program.ParametersMain.operationen,
                (
                    "3",
                    "drei",
                    "dreier",
                    "dreierstruktur",
                ),
                {92, 93},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                (
                    "Strukturgrösse",
                    "größe",
                    "groesse",
                    "gross",
                    "strukturgroesse",
                    "strukturgroeße",
                    "strukturgrösse",
                    "strukturgröße",
                ),
                {4, 21, 54, 197},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                ("Organisationen", "organisationen", "organisation"),
                {82},
            ),
            (
                Program.ParametersMain.strukturgroesse,
                ("politische_Systeme", "politischesysteme", "politik"),
                {83},
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("meta",),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        2,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("konkret",),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        2,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("Theorie", "theorie"),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        3,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("Praxis", "praxis"),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        3,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "Management",
                    "management",
                    "stau",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        4,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "verändernd",
                    "veraendernd",
                    "fluss",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        4,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("ganzheitlich", "mathematisch_diskret", "diskret"),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        5,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "darüber_hinausgehend",
                    "hinausgehend",
                    "kontinuierlich",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        5,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Universum_Strukturalien_Transzendentalien",
                    "universum",
                    "strukturalie",
                    "strukturalien",
                    "transzendentalien",
                    "transzendentalie",
                ),
                set(),
                set(),
                set(),
                set(),
                {(5,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Richtung_als_Richtung",
                    "richtungrichtung",
                ),
                set(),
                set(),
                set(),
                set(),
                {(None,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Galaxieabsicht",
                    "absichtgalaxie",
                    "absicht",
                    "motive",
                    "motiv",
                    "absichten",
                    "galaxie",
                ),
                set(),
                set(),
                set(),
                set(),
                {(10,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Absicht_Reziproke_Galaxie",
                    "absichtgalaxiereziproke",
                    "absichtreziproke",
                    "motivereziproke",
                    "motivreziproke",
                    "absichtenreziproke",
                    "galaxiereziproke",
                ),
                set(),
                set(),
                set(),
                set(),
                {(42,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Universum_Reziproke",
                    "universumreziproke",
                    "strukturaliereziproke",
                    "strukturalienreziproke",
                    "transzendentalienreziproke",
                    "transzendentaliereziproke",
                ),
                set(),
                set(),
                set(),
                set(),
                {(131,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "Dagegen-Gegentranszendentalie",
                    "dagegengegentranszendentalie",
                    "dagegengegentranszendentalien",
                    "dagegengegenstrukturalien",
                    "dagegengegenstrukturalie",
                ),
                set(),
                set(),
                set(),
                set(),
                {(138,)},
            ),
            (
                Program.ParametersMain.primzahlwirkung,
                (
                    "neutrale_Gegentranszendentalie",
                    "neutralegegentranszendentalie",
                    "neutralegegentranszendentalien",
                    "neutralegegenstrukturalien",
                    "neutralegegenstrukturalie",
                ),
                set(),
                set(),
                set(),
                set(),
                {(202,)},
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "Unternehmung_Geschäft",
                    "unternehmen",
                    "unternehmung",
                    "geschaeft",
                    "geschäft",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        6,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                ("wertvoll", "wert"),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        6,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "Beherrschen",
                    "regieren",
                    "beherrschen",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        7,
                        0,
                    )
                },
            ),
            (
                Program.ParametersMain.universummetakonkret,
                (
                    "Richtung",
                    "richtung",
                    "gut",
                ),
                set(),
                set(),
                set(),
                set(),
                {
                    (
                        7,
                        1,
                    )
                },
            ),
            (
                Program.ParametersMain.universum,
                (
                    "analytische_Ontologie",
                    "analytischeontologie",
                    "ontologie",
                ),
                {84},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "Gegentranszendentalien",
                    "gegentranszendentalien",
                    "gegentranszendentalie",
                    "gegenstrukturalien",
                    "gegenalien",
                    "gegenexistenzialien",
                    "gegenuniversalien",
                ),
                {138, 202},
            ),
            (
                Program.ParametersMain.universum,
                ("Systemsachen", "systemsachen"),
                {
                    150,
                },
            ),
            (
                Program.ParametersMain.universum,
                (
                    "Transzendentalien",
                    "transzendentalien",
                    "transzendentalie",
                    "strukturalien",
                    "alien",
                    "existenzialien",
                    "universalien",
                ),
                {5, 54, 55, 198},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "Reziproke_von_Transzendentalien",
                    "transzendentalienreziproke",
                    "transzendentaliereziproke",
                    "strukturalienreziproke",
                    "alienreziproke",
                    "existenzialienreziproke",
                    "universalienreziproke",
                ),
                {131, 201},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "warum_Transzendentalie_=_Strukturgroesse_=_Charakter",
                    "warumtranszendentaliezustrukturgroesseundcharakter",
                ),
                {4, 54, 5, 165},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "warum_Transzendentalie_=_Komplexität_von_Michael_Commons",
                    "warumtranszendentaliegleichkomplexitaet",
                ),
                {65, 5, 166},
            ),
            (
                Program.ParametersMain.universum,
                (
                    "Model_of_Hierarchical_Complexity",
                    "modelofhierarchicalcomplexity",
                    "komplex",
                    "komplexität",
                    "komplexitaet",
                    "complexity",
                    "model",
                    "abstraktion",
                ),
                {65, 75},
            ),
            (
                Program.ParametersMain.operationen,
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
                Program.ParametersMain.operationen,
                (
                    "Multiplikation",
                    "multiplikation",
                ),
                {158},
            ),
            (
                Program.ParametersMain.operationen,
                ("4", "vier", "viererstruktur", "viererabfolgen"),
                {76, 77, 81, 104, 145},
            ),
            (
                Program.ParametersMain.menschliches,
                ("Fachgebiete", "fachgebiete", "fachbereiche", "themen"),
                {183},
            ),
            (
                Program.ParametersMain.wirtschaft,
                ("Fachgebiete", "fachgebiete", "fachbereiche", "themen"),
                {183},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "Pflanzen",
                    "pflanzen",
                ),
                {113},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "Maschinen",
                    "maschinen",
                    "maschine",
                    "gerät",
                    "geräte",
                    "geraete",
                    "geraet",
                ),
                {89},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "Organisationsform",
                    "organisationsform",
                    "organisationsart",
                    "firma",
                    "verein",
                ),
                {99},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "System",
                    "system",
                ),
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
                    "Erklärung",
                    "erklärung",
                    "erklaerung",
                ),
                {71},
            ),
            (
                Program.ParametersMain.wirtschaft,
                (
                    "BWL",
                    "bwl",
                ),
                {109},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Sinn_des_Lebens",
                    "sinndeslebens",
                    "lebenssinn",
                    "sinn",
                    "sinnsuche",
                ),
                {88, 189},
                {(181, 182)},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Intelligenzprobleme",
                    "intelligenzprobleme",
                    "intelligenzmaengel",
                    "intelligenzmängel",
                ),
                {147},
            ),
            (
                Program.ParametersMain.menschliches,
                ("Denkweise_von_Lebewesen", "lebewesendenkweise", "denkweise"),
                {146},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Gegentranszendentalien",
                    "gegentranszendentalien",
                    "gegenstrukturalien",
                ),
                {138, 139, 202},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Gleichheit_Freiheit",
                    "gleichheitfreiheit",
                    "ungleichheit",
                    "dominieren",
                    "gleichheit",
                    "freiheit",
                ),
                {132},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Gefühle",
                    "emotionen",
                    "gefuehle",
                    "gefuehle",
                    "emotion",
                    "gefühl",
                    "gefuehl",
                ),
                {105},
            ),
            (
                Program.ParametersMain.menschliches,
                ("Egoismus", "egoismus", "altruismus", "selbstlosigkeit"),
                {136},
                {(66, 67)},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Wirkung",
                    "wirkung",
                ),
                {135},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "INCELs",
                    "incel",
                    "incels",
                ),
                {68},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "irrationale_Zahlen_durch_Wurzelbildung",
                    "irrationalezahlendurchwurzelbildung",
                    "ausgangslage",
                ),
                {73},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "dominierendes_Geschlecht",
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
                    "Liebe",
                    "liebe",
                    "ethik",
                ),
                {8, 9, 28},
                {(121, 122)},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Glaube_Erkenntnis",
                    "glauben",
                    "erkenntnis",
                    "glaube",
                ),
                {59},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Angreifbarkeit",
                    "angreifbarkeit",
                    "angreifbar",
                ),
                {58, 57},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Motive",
                    "motive",
                    "motivation",
                    "motiv",
                    "absicht",
                    "absichten",
                ),
                {10, 18, 42, 167, 168, 149},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Errungenschaften",
                    "errungenschaften",
                    "ziele",
                    "erhalten",
                ),
                {11},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "evolutionär_erwerben_und_Intelligenz_Kreativität",
                    "evolutionärerwerbenundintelligenz",
                    "intelligenz",
                    "erwerben",
                    "erlernen",
                    "lernen",
                    "evolutionaer",
                    "evolutionär",
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
                    "Krankheit",
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
                    "alpha_beta",
                    "alphabeta",
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
                    "Anführer",
                    "anfuehrer",
                    "chef",
                ),
                {29, 170},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Manipulation",
                    "manipulation",
                ),
                {153},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Berufe",
                    "berufe",
                    "beruf",
                ),
                {30},
            ),
            (
                Program.ParametersMain.menschliches,
                (
                    "Lösungen",
                    "lösungen",
                    "loesungen",
                    "loesung",
                    "lösungen",
                ),
                {31},
            ),
            (Program.ParametersMain.menschliches, ("Musik", "musik"), {33}),
            (
                Program.ParametersMain.procontra,
                (
                    "ergibt_Sinn",
                    "ergibtsinn",
                    "machtsinn",
                    "sinn",
                ),
                {140},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Veränderung",
                    "veraenderung",
                    "veraendern",
                    "veränderung",
                    "verändern",
                ),
                {142},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "bändigen_kontrollieren",
                    "baendigenkontrollieren",
                    "kontrollieren",
                    "baendigen",
                    "bändigen",
                ),
                {143},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "vereinen",
                    "einheit",
                ),
                {144},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Vorteile",
                    "vorteile",
                    "veraenderungnutzen",
                ),
                {141},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Gegenspieler",
                    "gegenspieler",
                    "antagonist",
                ),
                {137},
            ),
            (
                Program.ParametersMain.procontra,
                ("nervig",),
                {120},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "pro_nutzen",
                    "pronutzen",
                ),
                {117},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Gegenposition",
                    "gegenposition",
                ),
                {116},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Hilfe_erhalten",
                    "hilfeerhalten",
                ),
                {114},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Helfen",
                    "helfen",
                    "hilfe",
                ),
                {115},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Pro",
                    "pro",
                    "dafür",
                    "dafuer",
                ),
                {17, 48},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "nicht_miteinander_auskommen",
                    "nichtauskommen",
                ),
                {123},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "nicht_dagegen",
                    "nichtdagegen",
                ),
                {124},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "kein_Gegenteil",
                    "keingegenteil",
                ),
                {125},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "nicht_dafür",
                    "nichtdafuer",
                ),
                {126},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Hilfe_nicht_gebrauchen",
                    "hilfenichtgebrauchen",
                ),
                {127},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "nicht_helfen_können",
                    "nichthelfenkoennen",
                ),
                {128},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "nicht_abgeneigt",
                    "nichtabgeneigt",
                ),
                {129},
            ),
            (
                Program.ParametersMain.procontra,
                ("unmotivierbar",),
                {130},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "contra",
                    "dagegen",
                ),
                {15, 26},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Gegenteil",
                    "gegenteil",
                ),
                {100, 101},
            ),
            (
                Program.ParametersMain.procontra,
                (
                    "Harmonie",
                    "harmonie",
                ),
                {102, 103},
            ),
            (Program.ParametersMain.licht, (), {20, 27}),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Vorzeichen",
                    "vorzeichen",
                ),
                {118, 119},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Primzahlen",
                    "primzahlen",
                    "vielfache",
                    "vielfacher",
                ),
                {19},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Anwendung_der_Sonnen_und_Monde",
                    "anwendungdersonnenundmonde",
                    "anwendungdersonnen",
                    "anwendungenfuermonde",
                ),
                {22},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Zählungen",
                    "zählungen",
                    "zaehlung",
                    "zaehlungen",
                    "zählung",
                ),
                {25, 45, 169, 188},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Jura",
                    "jura",
                    "gesetzeslehre",
                    "recht",
                ),
                {34},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Vollkommenheit_des_Geistes",
                    "vollkommenheit",
                    "geist",
                ),
                {35},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Gestirn",
                    "gestirn",
                    "mond",
                    "sonne",
                    "planet",
                ),
                {64, 154},
                set(),
                set(),
                set(),
            ),
            (
                Program.ParametersMain.bedeutung,
                ("Konjunktiv_Wurzelbildung", "konjunktiv", "wurzel"),
                {106},
            ),
            (
                Program.ParametersMain.bedeutung,
                (
                    "Wesen_Züchten",
                    "wesen",
                    "zuechtung",
                    "züchtung",
                    "züchten",
                    "zuechten",
                ),
                {107, 108, 109},
            ),
            (
                Program.ParametersMain.gebrochengalaxie,
                set([str(a) for a in range(2, 100)]),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set([str(a) for a in range(2, 100)]),
            ),
            (
                Program.ParametersMain.gebrochenuniversum,
                set([str(a) for a in range(2, 100)]),
                set(),
                set(),
                set(),
                set(),
                set(),
                set([str(a) for a in range(2, 100)]),
            ),
            (Program.ParametersMain.symbole, (), {36, 37}),
            # (
            #    Program.ParametersMain.primzahlvielfachesgalaxie,
            #    allowedPrimNumbersForCommand,
            #    set(),
            #    set(),
            #    (
            #        lambda: {  # nur noch ein Platzhalter
            #            None,
            #        },
            #    ),
            # ),
            (
                Program.ParametersMain.konzept,
                (
                    "Weisheit_etc",
                    "weisheit",
                    "metaweisheit",
                    "meta-weisheit",
                    "idiot",
                    "weise",
                    "optimal",
                    "optimum",
                ),
                {112},
                {(40, 41)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Zuneigung_Abneigung",
                    "abgeneigt",
                    "zugewandt",
                    "reserviert",
                    "zugeneigt",
                ),
                set(),
                {(199, 200)},
            ),
            (
                Program.ParametersMain.konzept,
                ("wertvoll", "wertlos"),
                set(),
                {(186, 187)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Götter_Propheten_Familien_Freunde",
                    "familiaer",
                    "goettlich",
                    "freunde",
                    "propheten",
                ),
                set(),
                {(184, 185)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "sanft_vs_hart",
                    "sanft",
                    "hart",
                ),
                set(),
                {(159, 160), (161, 162)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "vereinen_vs_verbinden",
                    "vereinenverbinden",
                    "vereinen",
                    "verbinden",
                    "einheit",
                    "verbindung",
                ),
                set(),
                {(133, 134)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "gut_böse_lieb_schlecht",
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
                ("Sinn_und_Zweck_des_Lebens", "sinn", "zweck", "bedeutung"),
                {88, 189},
                {(181, 182)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Zeit_vs_Raum",
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
                    "egalitär_vs_autoritär",
                    "egalitaerautoritaer",
                    "egalitaer",
                    "autoritaer",
                    "egalitär",
                    "autoritär",
                ),
                set(),
                {(163, 164)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Meinungen_und_Ruf",
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
                    "Selbstgerechtigkeit",
                    "selbstgerechtigkeit",
                    "selbstgerecht",
                ),
                set(),
                {(62, 63)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Meinungsintelligenz", "meinungsintelligenz", "ursprungsintelligenz"),
                set(),
                {(151, 152)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Sittlichkeit", "sittlichkeit", "annaehrerung"),
                set(),
                {(179, 180)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Führung", "führung", "fuehrung"),
                set(),
                {(173, 174)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Durchleuchten", "durchleuchten", "erleuchten"),
                set(),
                {(177, 178)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Fördern", "foerdern", "fördern", "begrenzen"),
                set(),
                {(175, 176)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Überheblichkeit",
                    "überheblich",
                    "ueberheblichkeit",
                    "ueberheblich",
                    "überheblichkeit",
                ),
                set(),
                {(171, 172)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Polung_der_Liebe",
                    "liebepolung",
                ),
                set(),
                {(121, 122)},
            ),
            (
                Program.ParametersMain.konzept,
                (
                    "Egoismus_vs_Altruismus",
                    "egoismus",
                    "altruismus",
                    "egoist",
                    "altruist",
                ),
                {136},
                {(66, 67)},
            ),
            (Program.ParametersMain.konzept, ("kausal",), set(), {(110, 111)}),
            (
                Program.ParametersMain.konzept,
                ("Gleichheit", "gleich"),
                set(),
                {(192, 193)},
            ),
            (
                Program.ParametersMain.konzept,
                ("Überleben", "ueberleben"),
                set(),
                {(194, 195)},
            ),
            (Program.ParametersMain.inkrementieren, set(), {43, 54, 74, 95}),
            (Program.ParametersMain.inkrementieren, ("um1",), {155}),
            (Program.ParametersMain.inkrementieren, ("um2",), {156}),
            (Program.ParametersMain.inkrementieren, ("um3",), {157}),
            (
                Program.ParametersMain.inkrementieren,
                (
                    "warum_Transzendentalie_=_Strukturgroesse_=_Charakter",
                    "warumtranszendentaliezustrukturgroesseundcharakter",
                ),
                {4, 54, 5, 165},
            ),
            (
                Program.ParametersMain.inkrementieren,
                (
                    "warum_Transzendentalie_=_Komplexität_von_Michael_Commons",
                    "warumtranszendentaliegleichkomplexitaet",
                ),
                {65, 5, 166},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Motive_gleichförmige_Polygone", "motivgleichfoermig"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primMotivGleichf"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Struktur_gleichförmige_Polygone", "strukturgleichfoermig"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primStrukGleichf"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Motive_Sternpolygone", "motivstern"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primMotivStern"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Struktur_Sternpolygone", "strukturstern"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primStrukStern"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Motiv_Sternpolygon_gebrochen-rational", "motivgebrstern"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primMotivSternGebr"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Struktur_Sternpolyon_gebrochen-rational", "strukgebrstern"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primStrukSternGebr"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("Motiv_gleichförmige_Polygone_gebrochen-rational", "motivgebrgleichf"),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primMotivGleichfGebr"},
            ),
            (
                Program.ParametersMain.primvielfache,
                (
                    "Struktur_gleichförmige_Polygone_gebrochen-rational",
                    "strukgebrgleichf",
                ),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"primStrukGleichfGebr"},
            ),
            (
                Program.ParametersMain.primvielfache,
                ("beschrieben",),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                set(),
                {"PrimCSV"},
            ),
        ]

        """
        paraNdataMatrix4onlyGenerated: dict = {
            "primMotivGleichf": (
                ("Primzahlvielfache", "primvielfache"),
                ("Motive_gleichförmige_Polygone", "motivgleichfoermig"),
            ),
            "primStrukGleichf": (
                ("Primzahlvielfache", "primvielfache"),
                ("Struktur_gleichförmige_Polygone", "strukturgleichfoermig"),
            ),
            "primMotivStern": (
                ("Primzahlvielfache", "primvielfache"),
                ("Motive_Sternpolygone", "motivstern"),
            ),
            "primStrukStern": (
                ("Primzahlvielfache", "primvielfache"),
                ("Struktur_Sternpolygone", "strukturstern"),
            ),
            "primStrukGebrRat": (
                ("Primzahlvielfache", "primvielfache"),
                ("Struktur_gebrochen-rational", "strukturgebrochenrational"),
            ),
            "PrimCSV": (("Primzahlvielfache", "primvielfache"), ("beschrieben",)),
        }
        """

        Program.kombiParaNdataMatrix = {
            1: (
                "Lebewesen",
                "tiere",
                "tier",
                "lebewesen",
            ),
            2: ("Berufe", "berufe", "beruf"),
            3: (
                "Kreativität_und_Intelligenz",
                "kreativität",
                "intelligenz",
                "kreativitaet",
            ),
            4: (
                "Liebe",
                "liebe",
            ),
            5: (
                "Transzendentalien_Strukturalien",
                "transzendenz",
                "transzendentalien",
                "strukturalien",
                "alien",
            ),
            6: ("Primzahlkreuz", "leibnitz", "primzahlkreuz"),
            7: (
                "Männer",
                "männer",
                "maenner",
                "frauen",
            ),
            8: (
                "Persönlichkeit_evolutionär_erwerben",
                "evolution",
                "erwerben",
                "persoenlichkeit",
                "persönlichkeit",
            ),
            9: (
                "Religion",
                "religion",
                "religionen",
            ),
            10: ("Motive_Ziele", "motivation", "motive", "ziele", "ziel", "motive"),
            11: ("analytische_Ontologie", "analytischeontologie", "ontologie"),
            12: (
                "Emotionen",
                "emotionen",
                "gefuehle",
                "gefühle",
                "emotion",
                "gefühl",
                "gefühle",
            ),
            13: ("Personen", "personen", "berühmtheiten", "beruehmtheiten"),
            14: ("Wesen_Züchten", "wesen", "zuechten", "züchten"),
            15: (
                "Gegentranszendentalien",
                "gegentranszendentalien",
                "gegenstrukturalien",
            ),
            16: (
                "Wirtschaftssysteme",
                "wirtschaftssystem",
                "wirtschaftssysteme",
                "kombinierteswirtschaftssystem",
                "kombiniertewirtschaftssysteme",
            ),
        }

        self.kombiReverseDict: dict = {}
        for key, value in Program.kombiParaNdataMatrix.items():
            for valuesInValuess in value:
                self.kombiReverseDict[valuesInValuess] = key

        allValues = [set(), set(), set(), set(), set(), set(), set(), set()]
        for possibleCommands in paraNdataMatrix:
            for commandValue, aAllValue in zip(possibleCommands[2:], allValues):
                try:
                    aAllValue |= commandValue
                except TypeError:
                    pass
                    # alxp(type(commandValue))
                    # alxp(commandValue)

        """
        Folgende Schleife ist eigentlich unnötig.
        Sie ist für bool Werte da, wenn Sachen generiert werden.
        Ich brauche aber gerade den bool wert gar nicht mehr, weil es in
        diesem Fall auch anders geht, aber für die Zukunft kann das hilfreich sein.
        Also lasse ich es mal stehen!

        for possibleCommands in paraNdataMatrix:
            for commandValue, aAllValue in zip(possibleCommands[6:], allValues[4:]):
                aAllValue += [commandValue]
        # allValues[1] = allValues[2]
        """
        allValues[2] = set((int(pNum) for pNum in allowedPrimNumbersForCommand))
        allValues[3] = set(Program.kombiParaNdataMatrix.keys())
        allValues[5] = set(range(2, 100))
        allValues[6] = set(range(2, 100))

        """
        self.paraDictGenerated = {}
        self.paraDictGenerated4htmlTags = {}
        for key, value in paraNdataMatrix4onlyGenerated.items():
            for firstParameter in value[0][1:]:
                for secondParameter in value[1][1:]:
                    self.paraDictGenerated[(firstParameter, secondParameter)] = key
            self.paraDictGenerated4htmlTags[(value[0][0], value[1][0])] = key
            allValues[7] |= {key}
        """

        paraNdataMatrix += [
            (
                Program.ParametersMain.alles,
                (),
                *allValues,
            )
        ]
        """
        Hier wird erreicht, dass beide Dictionaries stückweise aufgefüllt werden.
        Aus den 3 voran gegangen Datenstrukturen werden 2 Dicts gemacht.
        """
        self.paraMainDict, self.paraDict = {}, {}
        for parameterEntry in paraNdataMatrix:
            into = intoParameterDatatype(
                parameterEntry[0],
                parameterEntry[1],
                tuple(
                    parameterEntryElement
                    for parameterEntryElement in parameterEntry[2:]
                ),
            )
            self.paraDict, self.dataDict = mergeParameterDicts(
                self.paraMainDict,
                self.paraDict,
                self.dataDict,
                *into,
            )

        self.dataDict[3] = Program.kombiParaNdataMatrix

        # alxp(self.paraDictGenerated)
        # alxp("-|-|")
        # alxp(self.paraDictGenerated4htmlTags)
        # alxp("||-|")
        # alxp(self.paraDict)
        # alxp("--|-")
        # alxp(self.dataDict)
        # alxp("--||")
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
                if shellRowsAmount > self.tables.textWidth + 6 or shellRowsAmount <= 0
                else shellRowsAmount - 6
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
        self.dataDict: list = [{}, {}, {}, {}, {}, {}, {}, {}]
        self.spaltenTypeNaming: namedtuple = namedtuple(
            "SpaltenTyp",
            "ordinary generated1 concat1 kombi1 boolAndTupleSet1 gebroUni1 gebrGal1 generated2 ordinaryNot generate1dNot concat1Not kombi1Not boolAndTupleSet1Not gebroUni1Not gebrGal1Not generated2Not",
        )
        self.spaltenTypeNaming = self.spaltenTypeNaming(
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 6),
            (0, 7),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
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
            (0, 5): set(),
            (0, 6): set(),
            (0, 7): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (1, 3): set(),
            (1, 4): set(),
            (1, 5): set(),
            (1, 6): set(),
            (1, 7): set(),
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
        self.onlyGenerated = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.boolAndTupleSet1
        ]
        self.gebrUni = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.gebroUni1
        ]
        self.gebrGal = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.gebrGal1
        ]
        ones = []
        for a in self.onlyGenerated:
            if len(a) == 1:
                ones += a
        self.tables.getConcat.ones = ones
        # x("OnEs", self.tables.getConcat.ones)

        for gebrUniva in self.gebrUni:
            self.tables.gebrUnivSet.add(gebrUniva)
        for prims in self.puniverseprims:
            self.tables.primUniversePrimsSet.add(prims)

        if len(self.rowsOfcombi) > 0:
            paramLines.add("ka")
        self.tables.generRows = self.generRows
        self.tables.getPrepare.rowsAsNumbers = self.rowsAsNumbers
        self.tables.getOut.rowsAsNumbers = self.rowsAsNumbers

        self.tables.SpaltenVanillaAmount = len(self.rowsAsNumbers)

        CsvTheirsSpalten: dict = {}
        for i, input1 in enumerate(
            [
                self.puniverseprims,
                self.gebrUni,
                self.gebrGal,
                self.gebrUni,
                self.gebrGal,
            ],
            start=1,
        ):
            (
                self.relitable,
                rowsAsNumbers,
                CsvTheirsSpalten[i],
            ) = self.tables.getConcat.readConcatCsv(
                self.relitable, self.rowsAsNumbers, input1, i
            )
        primSpalten = CsvTheirsSpalten[1]
        gebrUnivSpalten = CsvTheirsSpalten[2]
        gebrGalSpalten = CsvTheirsSpalten[3]
        gebrUnivSpalten2 = CsvTheirsSpalten[4]
        gebrGalSpalten2 = CsvTheirsSpalten[5]

        self.relitable, self.rowsAsNumbers = self.tables.getConcat.concatRowsOfConcepts(
            self.relitable, self.tables.generRows, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatVervielfacheZeile(
            self.relitable, self.rowsAsNumbers
        )
        # x("294", self.rowsAsNumbers)
        self.relitable, self.rowsAsNumbers = self.tables.getConcat.concatModallogik(
            self.relitable, self.tables.generRows, self.rowsAsNumbers
        )
        # x("294", self.rowsAsNumbers)
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

        paraTextNamen = {}
        for text in self.spaltenArtenKey_SpaltennummernValue[(0, 7)]:
            paraTextNamen[text] = [self.dataDict[7][text]]

        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concat1RowPrimUniverse2(
            self.relitable,
            self.rowsAsNumbers,
            self.spaltenArtenKey_SpaltennummernValue[(0, 7)],
            paraTextNamen,
        )

        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatLovePolygon(self.relitable, self.rowsAsNumbers)
        (
            self.relitable,
            rowsAsNumbers,
        ) = self.tables.getConcat.spalteFuerGegenInnenAussenSeitlichPrim(
            self.relitable, self.rowsAsNumbers
        )

        couplesX = []
        for a in self.onlyGenerated:
            if len(a) == 2:
                couplesX += [a]

        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.spalteMetaKontretTheorieAbstrakt_etc_1(
            self.relitable, self.rowsAsNumbers, couplesX
        )

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
            primSpalten,
            gebrUnivSpalten,
            gebrGalSpalten,
            gebrUnivSpalten2,
            gebrGalSpalten2,
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
            primSpalten,
            gebrUnivSpalten,
            gebrGalSpalten,
            gebrUnivSpalten2,
            gebrGalSpalten2,
        ) = self.bringAllImportantBeginThings(argv)
        self.tables.getMainTable.createSpalteGestirn(self.relitable, self.rowsAsNumbers)
        # x("2943", self.rowsAsNumbers)
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
            primSpalten=primSpalten,
            gebrUnivSpalten=gebrUnivSpalten,
            gebrGalSpalten=gebrGalSpalten,
            gebrUnivSpalten2=gebrUnivSpalten2,
            gebrGalSpalten2=gebrGalSpalten2,
        )
        # x("2944", self.rowsAsNumbers)
        # x("2944", self.relitable[0][92])
        # x("2944", len(self.relitable[0]))
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
            """Ich könnte die <td> class parameter auf der ersten bzw. nullten Spalte belassen, anstelle diese Redundanz zu halten: deutlich kleinere html"""
        )
        alxp(
            """Viele Routinen schreiben, die Codeteile immer dann überspringen, wenn man weiß, dass sie nicht benötigt werden, zur Geschwindigkeitssteigerung"""
        )
        alxp("""Ctrl+C kontrollierter abbrechen lassen!""")
        # alxp("""2 mal pro seitlich = können (2) seitlich""")
        alxp("""Pytest verwenden wegen Geschwindigkeitstests.""")
        # alxp(
        #    "1. http://goexchange.de/viewtopic.php?f=13&t=2683#p17239 () \n    9. anderen etwas vormachen können (Bahai)\n    1/9. den anderen Strukturgrößen außer der Einheit (9, 1/9) etwas vormachen können"
        # )
        alxp("""aus der ergebnis relitable ein dict machen !!!! bestes !!! """)
        alxp(
            """breiten geht nicht richtig und zeilenumbruch funktioniert oft nicht bei zu breit, warum nur"""
        )
        alxp(
            """In einigen GenerierungsSpalten werden Teile aus der Reli dings kopiert, was unnötig ist.
             Außerem, dass dann die relitable ganz geklont werden muss. Und die Einzelsachen
             müssten nur selbst geklont werden und mehr nicht."""
        )
        alxp
        alxp(
            """Immer dann wenn ich die ganze relitable matrix deepcopy geklont habe, hätte ich das gar nicht tun müssen, da ich einfach nur die werte, die ich vorher raus genommen habe, einfach nur per copy oder deepcopy hätte nur rausnehmen müssen"""
        )
        alxp(
            "Ich muss bei vielen Funktionen noch den Funktionskopf, Quellcode hier dokumentieren"
        )
        alxp("vim: iIaAoOjJ mit Registern arbeiten wegen Löschen ohne ausschneiden")
        alxp(
            """ Überlegen wo ich besser Hashmaps statt Listen verwenden sollte oder Tuple. Die meisten Listen durch Dicts ersetzen: fast immer schneller! """
        )
        alxp(
            "Die Geschwindigkeitsteigerugnen entstehn meist durch anschließndes Zusammenfügen zu einer dann festen Größe."
        )
        alxp(
            """py datei erstellen, die dafür da ist datenstrukturen für die js zu bilden, die für die Zeilenangelegenheiten da sind, so dass die js die nicht jedes Mal berechnen muss."""
        )
        alxp(
            """Ich müsste wirklich noch total überall schauen und zu jedem Punkt im Forum zu gleichförmiges-Polygon-Religionen"""
        )
        alxp(
            """Ich könnte die Klasse immer nur ein mal definieren und dann per js auf alle in der gleichen Reihe die gleichen Tags dazu machen. Das geht schnell, macht die html kleiner, aber eigentlich beschleunigt das nichts wirklich, außer langsames Internet"""
        )
        # x("__", self.tables.htmlOutputYes)

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
        # x("AAAC1", animalsProfessionsTable)
        # x("AAAC2", "ENDDD")
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
            reliTableLenUntilNow=len(newTable[0]) - len(self.rowsOfcombi),
        )
        # x("AAAD1", newTable_kombi_1)
        # x("AAAD2", "ENDDD")
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

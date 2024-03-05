#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import copy
from enum import Enum


class ST(Enum):
    """Spalten Tag"""

    sternPolygon = 0
    gleichfoermigesPolygon = 1
    keinPolygon = 2
    galaxie = 3
    universum = 4
    keinParaOdMetaP = 5
    gebrRat = 6


tableTags = {
    frozenset({ST.keinParaOdMetaP, ST.sternPolygon, ST.galaxie}): {
        370,
        411,
        241,
        394,
        395,
        424,
    },
    frozenset(
        {ST.universum, ST.keinParaOdMetaP, ST.sternPolygon, ST.gleichfoermigesPolygon}
    ): {14},
    frozenset({ST.sternPolygon, ST.galaxie, ST.universum, ST.keinParaOdMetaP}): {
        318,
        4,
        20,
        15,
        26,
        140,
        142,
        143,
        144,
        141,
        137,
        120,
        114,
        115,
        116,
        117,
        17,
        48,
        123,
        124,
        125,
        126,
        127,
        128,
        129,
        130,
        100,
        101,
        102,
        103,
        222,
        36,
        21,
        4,
        422
    },
    frozenset(
        {ST.gleichfoermigesPolygon, ST.galaxie, ST.universum, ST.keinParaOdMetaP}
    ): {
        319,
        328,
        331,
        335,
        313,
        37,
        197,
    },
    frozenset({ST.gleichfoermigesPolygon, ST.sternPolygon, ST.keinParaOdMetaP}): {},
    frozenset({ST.gleichfoermigesPolygon, ST.galaxie, ST.keinParaOdMetaP}): {272, 379},
    frozenset({ST.gleichfoermigesPolygon, ST.keinParaOdMetaP}): {
        284,
        285,
        332,
        334,
        342,
        257,
        330,
        352,
        378,
        392,
        400,
        401,
        326,
        327,
        416,
        428
    },
    frozenset({ST.gleichfoermigesPolygon, ST.keinParaOdMetaP, ST.universum}): {
        205,
        346,
    },
    frozenset({ST.sternPolygon, ST.keinParaOdMetaP, ST.universum}): {
        132,
        213,
        107,
        214,
        235,
        240,
        230,
        264,
        314,
        351,
        387,
        385,
        204,
    },
    frozenset({ST.sternPolygon, ST.keinParaOdMetaP}): {
        232,
        233,
        234,
        243,
        249,
        250,
        251,
        252,
        253,
        254,
        255,
        256,
        260,
        261,
        262,
        263,
        265,
        266,
        267,
        268,
        269,
        270,
        271,
        272,
        276,
        282,
        283,
        286,
        287,
        288,
        289,
        290,
        293,
        294,
        295,
        296,
        298,
        299,
        300,
        301,
        302,
        305,
        306,
        309,
        310,
        311,
        312,
        317,
        321,
        322,
        323,
        324,
        325,
        333,
        336,
        337,
        339,
        341,
        343,
        344,
        345,
        347,
        348,
        349,
        350,
        353,
        354,
        356,
        357,
        340,
        8,
        9,
        28,
        208,
        384,
        388,
        389,
        391,
        393,
        396,
        397,
        398,
        399,
        404,
        405,
        410,
        412,
        413,
        414,
        415,
        338,
        281,
        377,
        402,
        403,
        406,
        407,
        408,
        417,
        418,
        419,
        420,
        421,
        423,
        425,
        427
    },
    frozenset({ST.sternPolygon, ST.galaxie}): {
        0,
        1,
        2,
        3,
        6,
        7,
        10,
        11,
        12,
        13,
        14,
        18,
        19,
        22,
        23,
        24,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        38,
        39,
        40,
        41,
        43,
        44,
        45,
        46,
        47,
        49,
        50,
        51,
        56,
        57,
        59,
        60,
        61,
        62,
        63,
        64,
        66,
        67,
        68,
        71,
        72,
        73,
        74,
        78,
        79,
        82,
        83,
        85,
        86,
        88,
        89,
        90,
        91,
        92,
        95,
        96,
        97,
        98,
        99,
        105,
        106,
        108,
        109,
        110,
        111,
        112,
        113,
        118,
        119,
        121,
        122,
        133,
        134,
        136,
        139,
        146,
        147,
        151,
        152,
        153,
        159,
        160,
        163,
        164,
        170,
        171,
        172,
        173,
        174,
        175,
        176,
        177,
        178,
        179,
        180,
        181,
        182,
        183,
        184,
        185,
        186,
        187,
        189,
        192,
        193,
        194,
        195,
        199,
        200,
        207,
        211,
        212,
        215,
        217,
        274,
        275,
        303,
        307,
        315,
        316,
    },
    frozenset({ST.universum, ST.sternPolygon}): {
        5,
        25,
        65,
        77,
        80,
        81,
        84,
        93,
        94,
        104,
        138,
        158,
        169,
        190,
        191,
        196,
        198,
        202,
        206,
        209,
        210,
        219,
        223,
        229,
        230,
        242,
        244,
        297,
        304,
        308,
        320,
        382,
        390,
        409,
        386,
        27,
        69,
        70,
        55,
        426
    },
    frozenset({ST.galaxie, ST.gleichfoermigesPolygon}): {
        16,
        42,
        58,
        148,
        161,
        162,
        237,
    },
    frozenset({ST.universum, ST.gleichfoermigesPolygon, ST.sternPolygon}): {},
    frozenset({ST.galaxie, ST.gleichfoermigesPolygon, ST.sternPolygon}): {
        52,
        53,
        87,
        154,
        167,
        168,
    },
    frozenset({ST.galaxie, ST.universum, ST.gleichfoermigesPolygon}): {329},
    frozenset({ST.galaxie, ST.universum, ST.sternPolygon}): {
        54,
        75,
        76,
        135,
        145,
        149,
        150,
        155,
        156,
        157,
        165,
        166,
        218,
        220,
        226,
        188,
    },
    frozenset({ST.universum, ST.gleichfoermigesPolygon}): {
        131,
        201,
        203,
        231,
        273,
        383,
    },
    frozenset({ST.universum, ST.galaxie, ST.gleichfoermigesPolygon, ST.sternPolygon}): {
        216
    },
}

# 65 = michael commons hauptspalte
# 82 Organisationen wie SOZ
# 93 = Galaxie Dreierstrukur * Zweierstruktur
# 100 = Gegenteil bzw. „ergibt zusammen keinen Sinn“ (Abstand: 5*2) (negative Zahlen sind Antitranszendentalien und nicht "böse nach außen")
# 110 111 = Kausal, Leibnitz: Geltung + Genese
# 120 = 3*3=9, größere Zahl fühlt sich genervt, gestört, regt sich auf, wird griesgrämig wegen niedrigerer Zahl
# 130 = 19*1 Abstand „niederes nicht motivieren können“ (negative Zahlen sind Antitranszendentalien und nicht "böse nach außen")
# 137 Gegenspieler = Antagonisten
# 144 = 2*3*3=18 „kann vereinen“, „nutzt zum Vorteil“
# 150 = Systemsachen (Typen 13,14,15)
# 157 = Inkrementieren um 3
# 158 steht schon drin
# 166 = Warum die Transzendentalie zu der Komplexitäts-Sache von Michael Commons (und darüber hinaus, höher) gehört
# 170 = Herrschaft (7 und oder 7*n) über welche Spezies


tableTags_kombiTable = {
    frozenset({ST.galaxie, ST.sternPolygon, ST.gleichfoermigesPolygon}): {
        1,
        2,
        3,
        7,
        8,
        9,
        10,
        12,
        13,
        16,
        17,
    },
    frozenset({ST.universum, ST.galaxie, ST.sternPolygon, ST.gleichfoermigesPolygon}): {
        5,
        6,
        11,
        15,
    },
}


tableTags_kombiTable2 = {
    frozenset({ST.universum, ST.galaxie, ST.sternPolygon, ST.gleichfoermigesPolygon}): {
        5
    },
    frozenset({ST.universum, ST.gleichfoermigesPolygon, ST.sternPolygon}): {
        1,
        2,
        3,
        4,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        15,
        16,
        17,
        18,
    },
}


def dictViceversa(dic: dict) -> dict:
    newDict = {}
    for key, value in dic.items():
        for number in value:
            newDict[int(number)] = copy(key)
    return newDict


tableTags2 = dictViceversa(tableTags)
tableTags2_kombiTable = dictViceversa(tableTags_kombiTable)
tableTags2_kombiTable2 = dictViceversa(tableTags_kombiTable2)


"""
Hier sind die ganzen Spaltennummern enthalten:
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
So heißen die dazu gehörignen Benennungen:
self.spaltenTypeNaming: namedtuple = namedtuple(
            "SpaltenTyp",
            "ordinary generated1 concat1 kombi1 boolAndTupleSet1 ordinaryNot generate1dNot concat1Not kombi1Not boolAndTupleSet1Not",
        )
oder so:
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
"""

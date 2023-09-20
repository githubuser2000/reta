#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../libs"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import reta

program = reta.Program(["reta", "-nichts"])
alles = program.AllSimpleCommandSpalten
allesMax = max(alles)
allesMin = min(alles)
allesRange = range(allesMin, allesMax + 1)
allesRangeSet = set(allesRange)
allesRangeSetSubtract = allesRangeSet - alles
print(allesRangeSetSubtract)
print(len(allesRangeSetSubtract))
allesBefehl = ["reta", "-zeilen", "--vorhervonausschnitt=1", "-spalten", "--alles"]
program = reta.Program(allesBefehl, runAlles=False)
program.invertAlles()
program.run()

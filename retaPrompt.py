#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import reta
from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.completion import NestedCompleter, WordCompleter
from prompt_toolkit.styles import Style

retaProgram = reta.Program([sys.argv[0]])
print(str(retaProgram.mainParaCmds))
# Es gibt einen vi mode in dieser lib
# html_completer = WordCompleter(["<html>", "<body>", "<head>", "<title>"])
html_completer = NestedCompleter.from_nested_dict(
    {
        "show": {"version": None, "clock": None, "ip": {"interface": {"brief"}}},
        "exit": None,
    }
)
text = prompt(
    # print_formatted_text("Enter HTML: ", sep="", end=""), completer=html_completer
    "Enter HTML: ",
    completer=html_completer,
    wrap_lines=False,
    complete_while_typing=True,
    vi_mode=True,
)
print("You said: %s" % text, end=" ")

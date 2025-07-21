# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

from luaparser import ast
import json

import json
from typing import Generator

from antlr4 import InputStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener

from luaparser import printers
from luaparser.astnodes import *
from luaparser.builder import BuilderVisitor
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaParser import LuaParser
from luaparser.utils.visitor import *


def parse(source: str) -> Chunk:
    """Parse Lua source to a Chunk."""
    """
    We implement this function as a polyfill because the original
    luaparser.ast.parse function somehow automatically prints to stdout.

    Run test test/bin/unit/test_luaparser_ast_parse.py in verbose mode to see
    the issue. See the command below to run the test.

    pytest --run-verbose-luaparser -s test/bin/unit/test_luaparser_ast_parse.py
    """
    lexer = LuaLexer(InputStream(source))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ConsoleErrorListener())

    token_stream = CommonTokenStream(lexer, channel=Token.DEFAULT_CHANNEL)
    parser = LuaParser(token_stream)
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxException("syntax errors")
    else:
        v = BuilderVisitor(token_stream)
        val = v.visit(tree)
        return val



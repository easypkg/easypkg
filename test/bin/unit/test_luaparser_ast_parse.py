# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import luaparser.ast
import pytest

@pytest.mark.verbose_luaparser
def test_parse_modulefile_01():
    """
    Test parsing of a modulefile using luaparser.ast.parse.
    This test is marked as verbose_luaparser and will only run if the
    --run-verbose-luaparser option is provided to pytest.
    This is to avoid cluttering the test output with luaparser's
    automatic print statements during normal test runs.
    """

    modulefile_path = "test/share/lmod/modulefiles/01-GCCcore-15.1.0.lua"

    with open(modulefile_path, "r") as file:
        modulefile_string = file.read()

    modulefile_ast = luaparser.ast.parse(modulefile_string)



# -------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# -------------------------------------------------------------------------------------------------


import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--run-verbose-luaparser",
        action="store_true",
        default=False,
        help="Run (verbose) luaparser tests",
    )

def pytest_configure(config):
    # Register the marker to avoid warnings
    config.addinivalue_line(
        "markers",
        "verbose_luaparser: mark test as verbose luaparser test",
    )

def pytest_collection_modifyitems(config, items):
    # If the flag is set, don't skip anything
    if config.getoption("--run-verbose-luaparser"):
        return

    # Otherwise, skip all tests marked verbose_luaparser
    skipit = pytest.mark.skip(
        reason="Need --run-verbose-luaparser option to run (verbose) tests"
    )
    for item in items:
        if "verbose_luaparser" in item.keywords:
            item.add_marker(skipit)

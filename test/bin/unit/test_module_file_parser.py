# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

import easypkg

expected_output = {
        "whatis": [
            "Description: The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,\n as well as libraries for these languages (libstdc++, libgcj,...).",
            "Homepage: https://gcc.gnu.org/",
            "URL: https://gcc.gnu.org/"
            ],
        "conflict": [
            "GCCcore"
            ],
        "prepend_path": {
            "CMAKE_LIBRARY_PATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64",
            "CMAKE_PREFIX_PATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0",
            "LD_LIBRARY_PATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64",
            "LIBRARY_PATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64",
            "MANPATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/share/man",
            "PATH": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/bin",
            "XDG_DATA_DIRS": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/share"
            },
        "setenv": {
            "EBROOTGCCCORE": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0",
            "EBVERSIONGCCCORE": "15.1.0",
            "EBDEVELGCCCORE": "/home/testuser/.local/easybuild/software/GCCcore/15.1.0/easybuild/GCCcore-15.1.0-easybuild-devel"
            },
        "help": "\nDescription\n===========\nThe GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,\n as well as libraries for these languages (libstdc++, libgcj,...).\n\n\nMore information\n================\n - Homepage: https://gcc.gnu.org/\n"
        }

def test_parse_modulefile_01():
    modulefile_path = "test/share/lmod/modulefiles/01-GCCcore-15.1.0.lua"

    output = easypkg.lmod.parse_modulefile_to_json(modulefile_path)

    assert output == expected_output






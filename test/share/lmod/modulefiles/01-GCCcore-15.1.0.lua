-- SPDX-License-Identifier: Apache-2.0
-- Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>

help([[
Description
===========
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
 as well as libraries for these languages (libstdc++, libgcj,...).


More information
================
 - Homepage: https://gcc.gnu.org/
]])

whatis("Description: The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
 as well as libraries for these languages (libstdc++, libgcj,...).")
whatis("Homepage: https://gcc.gnu.org/")
whatis("URL: https://gcc.gnu.org/")
conflict("GCCcore")
prepend_path("CMAKE_LIBRARY_PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64")
prepend_path("CMAKE_PREFIX_PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0")
prepend_path("LD_LIBRARY_PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64")
prepend_path("LIBRARY_PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib")
prepend_path("LIBRARY_PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/lib64")
prepend_path("MANPATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/share/man")
prepend_path("PATH","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/bin")
prepend_path("XDG_DATA_DIRS","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/share")
setenv("EBROOTGCCCORE","/home/testuser/.local/easybuild/software/GCCcore/15.1.0")
setenv("EBVERSIONGCCCORE","15.1.0")
setenv("EBDEVELGCCCORE","/home/testuser/.local/easybuild/software/GCCcore/15.1.0/easybuild/GCCcore-15.1.0-easybuild-devel")

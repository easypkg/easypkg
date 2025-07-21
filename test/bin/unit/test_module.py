# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

import lmod.spider
import lmod
import subprocess


expected_module_list = {
        '/home/testuser/.local/easybuild/modules/all/Bison/3.8.2-GCCcore-15.1.0.lua': 'Bison/3.8.2-GCCcore-15.1.0',
        '/home/testuser/.local/easybuild/modules/all/Bison/3.8.2.lua': 'Bison/3.8.2',
        '/home/testuser/.local/easybuild/modules/all/GCC/15.1.0.lua': 'GCC/15.1.0',
        '/home/testuser/.local/easybuild/modules/all/GCCcore/15.1.0.lua': 'GCCcore/15.1.0',
        '/home/testuser/.local/easybuild/modules/all/M4/1.4.19-GCCcore-15.1.0.lua': 'M4/1.4.19-GCCcore-15.1.0',
        '/home/testuser/.local/easybuild/modules/all/M4/1.4.19.lua': 'M4/1.4.19',
        '/home/testuser/.local/easybuild/modules/all/M4/1.4.20.lua': 'M4/1.4.20',
        '/home/testuser/.local/easybuild/modules/all/binutils/2.44-GCCcore-15.1.0.lua': 'binutils/2.44-GCCcore-15.1.0',
        '/home/testuser/.local/easybuild/modules/all/binutils/2.44.lua': 'binutils/2.44',
        '/home/testuser/.local/easybuild/modules/all/flex/2.6.4-GCCcore-15.1.0.lua': 'flex/2.6.4-GCCcore-15.1.0',
        '/home/testuser/.local/easybuild/modules/all/flex/2.6.4.lua': 'flex/2.6.4',
        '/home/testuser/.local/easybuild/modules/all/help2man/1.49.3-GCCcore-15.1.0.lua': 'help2man/1.49.3-GCCcore-15.1.0',
        '/usr/share/lmod/lmod/modulefiles/Core/lmod.lua': 'lmod',
        '/usr/share/lmod/lmod/modulefiles/Core/settarg.lua': 'settarg',
        '/home/testuser/.local/easybuild/modules/all/zlib/1.3.1-GCCcore-15.1.0.lua': 'zlib/1.3.1-GCCcore-15.1.0',
        '/home/testuser/.local/easybuild/modules/all/zlib/1.3.1.lua': 'zlib/1.3.1'
        }

def test_module_list():
    """
    Test function for the module.
    This function is a placeholder for actual tests.
    """

    spider = lmod.spider.Spider()
    module_list = spider.get_modules()
    assert module_list == expected_module_list







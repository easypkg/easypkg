# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

import lmod.spider
import subprocess
import json


def convert(input_dir_list, output):
    print(f"Input: {input_dir_list}")
    print(f"Output: {output}")

    input_dir = input_dir_list[0][0]

    result = subprocess.run(
        ["/usr/share/lmod/8.7.55/libexec/spider", "--output=jsonSoftwarePage", input_dir],
        check=True,
        capture_output=True,
    )

    print(json.dumps(json.loads(result.stdout.decode()), indent=4))

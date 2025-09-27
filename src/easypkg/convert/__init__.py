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

    package_data = json.loads(result.stdout.decode())
    print(json.dumps(package_data, indent=2))

    for package in package_data:
        pass
        # print(f"Processing package: {package['package']}")
        #print(json.dumps(package, indent=2))

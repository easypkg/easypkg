# -------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# -------------------------------------------------------------------------------------------------

import easypkg.polyfill.luaparser
import luaparser.ast
import json

def parse_modulefile_to_json(modulefile_path):
    with open(modulefile_path, "r") as file:
        modulefile_string = file.read()

    modulefile_ast = easypkg.polyfill.luaparser.parse(modulefile_string)


    ast_json = None
    for index, node in enumerate(luaparser.ast.walk(modulefile_ast)):
        if index == 0:
            ast_json = json.loads((luaparser.ast.to_pretty_json(node)))["body"]["body"]
        else:
            break

    # print(json.dumps(ast_json, indent=4))

    output = {}

    output["whatis"] = []
    output["conflict"] = []
    output["prepend_path"] = {}
    output["setenv"] = {}

    for node in ast_json:
        if node["func"]["id"] == "help":
            output[node["func"]["id"]] = node["args"][0]["s"]

        elif node["func"]["id"] == "whatis":
            output[node["func"]["id"]].append(node["args"][0]["s"])

        elif node["func"]["id"] == "conflict":
            output[node["func"]["id"]].append(node["args"][0]["s"])

        elif node["func"]["id"] == "prepend_path":
            output[node["func"]["id"]][node["args"][0]["s"]] = node["args"][1]["s"]

        elif node["func"]["id"] == "setenv":
            output[node["func"]["id"]][node["args"][0]["s"]] = node["args"][1]["s"]
        else:
            raise ValueError(f"Unknown function {node['func']['id']}")

    return output



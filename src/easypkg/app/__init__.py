# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

import argparse
import easypkg.convert


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def make_wide(formatter, w=140, h=100):
    """Return a wider HelpFormatter, if possible."""
    try:
        # https://stackoverflow.com/a/5464440
        # beware: "Only the name of this class is considered a public API."
        kwargs = {"width": w, "max_help_position": h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        warnings.warn("argparse help formatter failed, falling back.")
        return formatter


def convert_parser(cp):
    cp.add_argument(
        "--input",
        nargs="+",
        action="append",
        required=True,
        help="Path to Easybuild Modules Files",
    )
    cp.add_argument("--output", type=str, required=True, help="Spack File")


def top_level_parser():
    """Argument parser for the module."""
    parser = argparse.ArgumentParser(
        description="A Connector for Spack and Easybuild",
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    cp = subparsers.add_parser(
        "convert",
        help="Convert between Spack and Easybuild formats",
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
    )

    convert_parser(cp)
    return parser


def main():
    parser = top_level_parser()
    args = parser.parse_args()

    if args.command == "convert":
        # Here you would call the function that handles the conversion
        print(f"Generating Spack {args.output} file from Easybuild modules at {args.input}")

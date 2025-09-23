#!/usr/bin/bash
# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

set -euo pipefail

print_help() {
  cat << EOF
Usage: build --image <name> --version <tag> --registry <url> [--cache <cache_dir>] [--help]

Options:
  --image     Name of the image to build (required)
  --version   Version tag for the image (required)
  --registry  Registry URL to push the image to (required)
  --cache     Optional image reference to speed up builds
  --help      Show this help message and exit

Examples:
  build --image myapp --version 1.0.0 --registry docker.io/myuser
  build --image backend --version latest --registry ghcr.io/org --cache ghcr.io
EOF
}


die() { echo "build: $*" >&2; exit 1; }

# Defaults (if any)
IMAGE=""
VERSION=""
REGISTRY=""
CACHE=""

# helper: require a value for the previous flag
require_value() {
  local flag="$1" val="${2-}"
  [[ -n "${val:-}" && "${val:0:1}" != "-" ]] || die "option '$flag' requires a value"
}

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h)
      print_help
      exit 0
      ;;
    --image)
      require_value "$1" "${2-}"
      IMAGE="$2"; shift 2
      ;;
    --image=*)
      IMAGE="${1#*=}"; shift
      ;;
    --version)
      require_value "$1" "${2-}"
      VERSION="$2"; shift 2
      ;;
    --version=*)
      VERSION="${1#*=}"; shift
      ;;
    --registry)
      require_value "$1" "${2-}"
      REGISTRY="$2"; shift 2
      ;;
    --registry=*)
      REGISTRY="${1#*=}"; shift
      ;;
    --cache)
      require_value "$1" "${2-}"
      CACHE="$2"; shift 2
      ;;
    --cache=*)
      CACHE="${1#*=}"; shift
      ;;
    --) # end of flags
      shift
      break
      ;;
    -*)
      die "unknown option: $1 (see --help)"
      ;;
    *)
      # Positional arg (if you later want to support any)
      die "unexpected positional argument: $1 (see --help)"
      ;;
  esac
done

# Validate required parameters
[[ -n "$IMAGE"   ]] || die "missing required option: --image (see --help)"
[[ -n "$VERSION" ]] || die "missing required option: --version (see --help)"
[[ -n "$REGISTRY" ]] || die "missing required option: --registry (see --help)"

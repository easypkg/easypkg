# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------
FROM  ghcr.io/easypkg/base:v1

# Install Catch2
RUN eb --optarch=GENERIC --robot --modules-tool Lmod .local/easybuild/easyconfigs/g/GCCcore/GCCcore-15.1.0.eb






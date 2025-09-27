# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------
FROM  ghcr.io/easypkg/base:v1

# Switch to root to install test dependencies
USER root

# Install tree
RUN yum install -y tree python3-requests python3-pyOpenSSL

# Switch back to testuser
USER testuser

# Install Test Dependencies
RUN pip install hatch


# Copying Easyconfigs
COPY easybuild/easyconfigs/c/Catch2/Catch2-3.8.1-GCCcore-14.3.0.eb /home/testuser/.local/easybuild/easyconfigs/c/Catch2/Catch2-3.8.1-GCCcore-14.3.0.eb

COPY easybuild/easyconfigs/o/OpenMPI/OpenMPI-5.0.7-GCC-14.3.0.eb /home/testuser/.local/easybuild/easyconfigs/o/OpenMPI/OpenMPI-5.0.7-GCC-14.3.0.eb

## Install CMake
#RUN eb --optarch=GENERIC --robot --modules-tool Lmod ~/.local/easybuild/easyconfigs/c/CMake/CMake-4.0.3-GCCcore-14.3.0.eb
#
## Install Catch2
#RUN eb --optarch=GENERIC --robot --modules-tool Lmod /home/testuser/.local/easybuild/easyconfigs/c/Catch2/Catch2-3.8.1-GCCcore-14.3.0.eb
#
## Install OpenMPI







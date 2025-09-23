# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------
FROM  rockylinux:9
SHELL ["/bin/bash", "-c"]

# Update system
RUN   yum update -y
RUN   yum install -y epel-release
RUN   dnf config-manager --set-enabled crb

# Install Development Tools and LMod
RUN   yum groupinstall -y "Development Tools"
RUN   yum install -y python3-pip Lmod which perl tar bzip2 python3-devel
RUN   ln -s /usr/share/lmod/8.7.55/libexec/lmod /usr/local/bin/lmod

# Setup User
RUN   useradd -ms /bin/bash testuser
WORKDIR /home/testuser
RUN   echo "module use /home/testuser/.local/easybuild/modules/all/" >> /home/testuser/.bashrc
RUN   chown testuser:testuser /home/testuser/.bashrc
USER  testuser
ENV   PATH="/home/testuser/.local/bin:${PATH}"
RUN   echo $PATH

# Instlal Easybuild
RUN   pip install easybuild

# Compile Toolchain
RUN   eb --optarch=GENERIC --robot --modules-tool Lmod .local/easybuild/easyconfigs/g/GCCcore/GCCcore-13.3.0.eb
RUN   eb --optarch=GENERIC --robot --modules-tool Lmod .local/easybuild/easyconfigs/g/GCCcore/GCCcore-14.2.0.eb

# Install Spack
RUN   git clone --depth=2 --branch=releases/v1.0 https://github.com/spack/spack.git ~/.local/spack
RUN   echo "source $HOME/.local/spack/share/spack/setup-env.sh" >> /home/testuser/.bashrc







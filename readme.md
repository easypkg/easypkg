<!--
- SPDX-License-Identifier: Apache-2.0
- Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
-->

# easypkg - a connector from easybuild to spack

The connector will allow users to use spack as a package manager for the modules from the underlying
easybuild framework.


## Test Setup

In order for people to test the connector without having to build GCC and other
stuff from scratch, we provide a test docker image that contains everything setup and ready to use.
The image has the following modules available:

```shell
------------------------------ /home/testuser/.local/easybuild/modules/all -------------------------
   Bison/3.8.2    GCCcore/14.3.0    GCCcore/15.1.0 (D)    M4/1.4.19    M4/1.4.20 (D)
   binutils/2.44    flex/2.6.4    zlib/1.3.1

------------------------------ /usr/share/lmod/lmod/modulefiles/Core --------------------------------
   lmod    settarg

```

```shell
docker pull ghcr.io/easypkg/base:v1
```

The image is augmented with its buildcache which is available at:

```shell
docker pull ghcr.io/easypkg/base:v1.buildcache
```

The images were built using the command:

```shell
docker buildx build --push \
    -t ghcr.io/easypkg/base:v1 \
    --cache-from type=registry,ref=ghcr.io/easypkg/base:v1.buildcache,mode=max  \
    -f setup/lib/container/v1/base.dockerfile .
```



















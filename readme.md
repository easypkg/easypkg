<!--
- SPDX-License-Identifier: Apache-2.0
- Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
-->

# easypkg - a connector from easybuild to spack

The connector will allow users to use spack as a package manager for the modules
from the underlying easybuild framework.

You can test the package using the docker image provided at

```
ghcr.io/easypkg/test-environment:latest
```

And one can run the tests by running the following commands in the repository
root

```
docker run -v $PWD:/data -it ghcr.io/easypkg/test-environment:latest /bin/bash
# Inside the container
cd /data
hatch --env test run -- pytest -s
```



## Test Setup

In order for people to test the connector without having to build GCC and other
stuff from scratch, we provide a test docker image that contains everything
setup and ready to use.

```bash
docker pull ghcr.io/jayeshbadwaik/easypkg-test:latest
```

The image contains the following:
1. A working installation of easybuild with the following modules
   - Bison/3.8.2-GCCcore-15.1.0
   - Bison/3.8.2
   - GCC/15.1.0
   - GCCcore/15.1.0
   - M4/1.4.19-GCCcore-15.1.0
   - M4/1.4.19
   - binutils/2.44-GCCcore-15.1.0
   - binutils/2.44
   - flex/2.6.4-GCCcore-15.1.0
   - flex/2.6.4
   - help2man/1.49.3-GCCcore-15.1.0
   - zlib/1.3.1-GCCcore-15.1.0
   - zlib/1.3.1

2. A working installation of spack with **no packages installed**




















# Environment

`environment.yml` defines a portable baseline for Python research. It avoids
machine-specific prefixes and build hashes so that it can be recreated on
another computer.

GPU-enabled PyTorch is intentionally not pinned here because GPU builds depend
on the operating system, driver, and CUDA runtime. Add it only after verifying
the target machine's compatibility.

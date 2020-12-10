
# Malicious PyPI package proof of concept

This package demonstrates what a malicious PyPI package could do to you :-)

What it does: It downloads a python file from a github gist and runs it. That
python file creates a file in your `/tmp`. Nothing really malicious, but you 
get the point.

I created it mainly to test methods of installing python packages without the
danger of running their `setup.py`. At the moment there seem to be none. Poetry
manages to at least determine the dependencies of packages without running
their `setup.py` files, but also uses pip internally when installing. 

As a workaround, you can forbid the usage of source distribution packages by
using the `--only-binary :all:` flag on your pip commands. Unfortunately, some
packages do not have a binary distribution and you will be unable to install
them with this flag.

Here are some more resources to read about the problem:

* [mschwager's 0wned package](https://github.com/mschwager/0wned)
* [Jordan Wright caught my package](https://prog.world/check-thousands-of-pypi-packages-for-malware/)

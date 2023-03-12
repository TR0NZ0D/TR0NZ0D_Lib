# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import pathlib

from setuptools import find_packages, setup  # type: ignore

BASE_DIR = pathlib.Path(__file__).parent.resolve()

long_description = (BASE_DIR / "README.md").read_text(encoding="utf-8")

requirements = [
    'cryptography',
    'requests',
    'python-dateutil'
]

setup(
    name='tr0nz0d',
    version='0.1.4',
    description="TR0NZ0D Lib is a library created in python to facilitate the use of some tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TR0NZ0D/TR0NZ0D_Lib',
    author='Gabriel Menezes de Antonio',
    author_email='tr0nz0d@tr0nz0d.com',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "Natural Language :: Portuguese (Brazilian)",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Security :: Cryptography",
        "Topic :: Printing",
        "Topic :: System :: Logging"
    ],
    keywords="tronzod, tr0nz0d, TR0NZ0D, TRONZOD, tools",
    packages=find_packages(where="src", exclude=["venv"]),
    package_dir={"": "src"},
    setup_requires=requirements,
    install_requires=requirements,
    tests_require=["unittest"],
    python_requires='>=3.10',
    license="MIT",
    project_urls={
        "Source": "https://github.com/TR0NZ0D/TR0NZ0D_Lib",
        "Project Info": "https://tr0nz0d.com/projetos/tr0nz0d-lib-python-library",
        "Bug Tracker": "https://github.com/TR0NZ0D/TR0NZ0D_Lib/issues",
        "Documentation (PT-BR)": "https://tr0nz0d.com/docs/tr0nz0d-lib-python-library/",
        "Change Log (PT-BR)": "https://tr0nz0d.com/docs/changes/tr0nz0d-lib-python-library/"
    }
)

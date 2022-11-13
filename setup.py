from setuptools import setup, find_packages
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

long_description = (BASE_DIR / "README.md").read_text(encoding="utf-8")

requirements = [
    'cryptography',
    'requests',
    'python-dateutil'
]

setup(
    name='tr0nz0d',
    version='0.1.0',
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
    packages=find_packages(where="tr0nz0d", exclude=["venv"]),
    package_dir={"": "tr0nz0d"},
    setup_requires=requirements,
    install_requires=requirements,
    tests_require=["unittest"],
    python_requires='>=3.10',
    license="MIT",
    project_urls={
        "Source": "https://github.com/TR0NZ0D/TR0NZ0D_Lib",
        "Project Info": "https://tr0nz0d.com/projetos/tr0nz0d-lib-python-library",
        "Bug Tracker": "https://github.com/TR0NZ0D/TR0NZ0D_Lib/issues",
        "Documentation (PT-BR)": "https://tr0nz0d.github.io/pages/projetos/projeto/libs/docs/lib-index.html",
        "Change Log (PT-BR)": "https://tr0nz0d.github.io/pages/projetos/projeto/libs/docs/pages/changelog.html"
    }
)

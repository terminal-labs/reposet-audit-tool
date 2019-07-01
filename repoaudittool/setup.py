import sys
from setuptools import setup

assert sys.version_info >= (3, 6, 0)

setup(
    name="repo-audit-tool",
    version="0.0.1",
    description="repo audit tool",
    url="https://github.com/terminal-labs/repo-audit-tool",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="see LICENSE file",
    packages=["repoaudittool", "tests"],
    zip_safe=False,
    install_requires=["coverage",
        "pycontracts",
        "pytest",
        "pytest-cov",
        "pytest-mock",
        "pytest-click",
        "pytest-pylint",
        "black",
        "flake8",
        "radon",
    ],
)

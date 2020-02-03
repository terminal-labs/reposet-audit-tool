import sys
from setuptools import setup, find_packages

from repoaudittool.settings import *

assert sys.version_info >= (3, 6, 0)

setup(
    name="repo-audit-tool",
    version=VERSION,
    description="repo audit tool",
    url="https://github.com/terminal-labs/repo-audit-tool",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="mit",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
    ],
    entry_points="""
        [console_scripts]
        repoaudittool=repoaudittool.__main__:main
    """,
)

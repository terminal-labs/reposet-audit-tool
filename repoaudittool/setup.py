import sys
from setuptools import setup

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
    packages=["repoaudittool", "repoaudittool.tests"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
                      "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
                      "PyGithub",
                    ],
    entry_points="""
        [console_scripts]
        repoaudittool=repoaudittool.__main__:main
    """,
)

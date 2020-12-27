import sys
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

package_link = '.tmp/symlink'

setup(
    name="repoaudittool",
    version="0.0.1",
    description="repo audit tool",
    url="https://github.com/terminal-labs/repo-audit-tool",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="mit",
    package_dir={'': package_link},
    packages=find_packages(where=package_link),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "utilities-package-pinion@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package-pinion.git",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
    ],
    entry_points="""
        [console_scripts]
        repoaudittool=repoaudittool.__main__:main
    """,
)

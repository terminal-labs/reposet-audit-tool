import sys
import configparser
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

config = configparser.ConfigParser()
config.read("setup.cfg")

version = config["metadata"]["version"]
name = config["metadata"]["name"]

setup_author="Terminal Labs",
setup_author_email="solutions@terminallabs.com",
setup_license="see LICENSE file",
setup_url = "https://github.com/terminal-labs/repo-audit-tool"
package_link = ".tmp/symlink"

repo_name = name
package_name = repo_name.replace("-","")
setup_stub_name = package_name
setup_full_name = repo_name
setup_description = setup_full_name.replace("-"," ")

pins = []

reqs = [
    "setuptools",
    "utilities-package-pinion@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package-pinion.git",
    "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
]

setup(
    name=setup_full_name,
    version=version,
    description=setup_description,
    url=setup_url,
    author=setup_author,
    author_email=setup_author_email,
    license=setup_license,
    package_dir={'': package_link},
    packages=find_packages(where=package_link),
    zip_safe=False,
    include_package_data=True,
    install_requires=pins + reqs,
    entry_points=f"""
        [console_scripts]
        repoaudittool=repoaudittool.__main__:main
    """,
)

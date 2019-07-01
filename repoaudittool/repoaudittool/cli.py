import os
import click
import pytest
import requests

from repoaudittool.settings import *


@click.group()
def cli():
    return None


@click.group(name="scanrepos")
def scanrepos_group():
    return None


@click.group(name="system")
def system_group():
    return None


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(SETUPFILEDIR)
    pytest.main(["-x", "-v", SETUPFILEDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(SETUPFILEDIR)
    pytest.main(["--cov-config=" + COVERAGERC_PATH, "--cov=repoaudittool", "--cov-report", "term-missing", SETUPFILEDIR])


cli.add_command(scanrepos_group)
cli.add_command(system_group)
main = cli

if __name__ == "__main__":
    main()

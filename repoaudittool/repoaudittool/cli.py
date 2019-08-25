import os
import click
import pytest
import requests

from repoaudittool.settings import *
from repoaudittool.app import load_manifest_dir


@click.group()
def cli():
    return None


@click.group(name="scanrepos")
def scanrepos_group():
    return None


@click.group(name="system")
def system_group():
    return None


@scanrepos_group.command(name="scan")
@click.argument('dirpath')
def scanrepos(dirpath):
    print(load_manifest_dir(dirpath))


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(TESTDIR)
    pytest.main(["-x", "-v", TESTDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(APPDIR)
    pytest.main([f"--cov-config={COVERAGERC_PATH}", "--cov=repoaudittool", "--cov-report", "term-missing", APPDIR])


cli.add_command(scanrepos_group)
cli.add_command(system_group)
main = cli

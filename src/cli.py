import os
import click

import pytest
import requests

with open(os.path.dirname(__file__) + "/framework/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
mod = f"{_pgk_name}.framework.layout"
showlayout = _import_fun(mod, "showlayout")

_pgk_name = _get_pgk_name()
mod = f"{_pgk_name}.framework.settings"
VERSION = _import_fun(mod, "VERSION")
COVERAGERC_PATH = _import_fun(mod, "COVERAGERC_PATH")

mod = f"{_pgk_name}.framework.derived_settings"
APPDIR = _import_fun(mod, "APPDIR")
TESTDIR = _import_fun(mod, "TESTDIR")

mod = f"{_pgk_name}.app"
load_manifest_dir = _import_fun(mod, "load_manifest_dir")
load_sync_dir = _import_fun(mod, "load_sync_dir")
clone_repo = _import_fun(mod, "clone_repo")
clone_repo_for_syncing = _import_fun(mod, "clone_repo_for_syncing")
sync = _import_fun(mod, "sync")
audit_repos = _import_fun(mod, "audit_repos")
dir_delete = _import_fun(mod, "dir_delete")


@click.group()
def cli():
    return None


@click.group(name="scanrepos")
def scanrepos_group():
    return None


@click.group(name="syncrepos")
def syncrepos_group():
    return None


@click.group(name="system")
def system_group():
    return None


@scanrepos_group.command(name="scan")
@click.argument("dirpath")
def scanrepos(dirpath):
    manifest_dict = load_manifest_dir(dirpath)
    clone_repo(manifest_dict)
    audit_repos(manifest_dict)


@syncrepos_group.command(name="sync")
@click.argument("dirpath")
def syncrepos(dirpath):
    manifest_list = load_sync_dir(dirpath)
    clone_repo_for_syncing(manifest_list)
    sync(manifest_list)


@system_group.command(name="showlayout")
def showlayout_command():
    print(*showlayout().items(), sep='\n')


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
    pytest.main(
        [
            f"--cov-config={COVERAGERC_PATH}",
            f"--cov={_pgk_name}",
            "--cov-report",
            "term-missing",
            APPDIR,
        ]
    )


cli.add_command(scanrepos_group)
cli.add_command(syncrepos_group)
cli.add_command(system_group)
main = cli

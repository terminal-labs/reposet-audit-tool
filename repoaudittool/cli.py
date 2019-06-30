import click
import requests

VERSION = "0.1"

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


cli.add_command(scanrepos_group)
cli.add_command(system_group)
main = cli

if __name__ == "__main__":
    main()

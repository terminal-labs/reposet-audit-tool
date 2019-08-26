import os
import sys
import binascii
import pickle
import glob
import yaml

from bash import bash

from repoaudittool.utils import create_dir
from repoaudittool.constants import HOURS_IN_WEEK
from repoaudittool.settings import *


def dir_create(path):
    if not os.path.exists(path):
        os.makedirs(path)


def system_check():
    assert sys.version_info >= MINIMUM_PYTHON_VERSION


def initialize():
    for dir in DIRS:
        create_dir(dir)


def clone_repo(manifest_dict):
    dir_create("/tmp/rat")
    for file in manifest_dict['reponames']:
        dir_create("/tmp/rat/" + file)
        bash(f"cd /tmp/rat/{file}; git clone git@github.com:terminal-labs/{file}.git")


def load_yaml_files(dirpath, repospecs):
    specs = []
    for repospec in repospecs:
        specs.append(yaml.load(open(dirpath + "/specs/" + repospec), Loader=yaml.FullLoader))
    return specs


def scan_for_requiredfiles(reponame, requiredfiles):
    print(reponame, requiredfiles)


def audit_repos(manifest_dict):
    for repo in manifest_dict["reponames"]:
        scan_for_requiredfiles(repo, manifest_dict["specs"][repo]['spec']['requiredfiles'])


def load_manifest_dir(dirpath):
    manifest_dict = {}
    if os.path.isdir(dirpath):
        files = os.listdir(dirpath)
        if "repos.txt" in files:
            f = open(dirpath + "/repos.txt", "r")
            lines = f.readlines()
            names = [line.split(' ')[0] for line in lines]
            names = [name.strip() for name in names]
            manifest_dict["reponames"] = names
            repospecs = [line.split(' ')[1] for line in lines]
            repospecs = [repospec.strip() for repospec in repospecs]

            manifest_dict["repospecsmap"] = {}
            i = 0
            while i < len(lines):
                manifest_dict["repospecsmap"][names[i]] = repospecs[i]
                i = i + 1

            manifest_dict["specs"] = {}
            specs = load_yaml_files(dirpath, repospecs)
            i = 0
            while i < len(lines):
                manifest_dict["specs"][names[i]] = specs[i]
                i = i + 1


        return manifest_dict

import os
import sys
import binascii
import pickle
import glob
import hashlib
from pathlib import Path
from shutil import copyfile, move, rmtree

import yaml
from bash import bash

from repoaudittool.settings import *

tempdir = "/tmp/rat/"

def dir_create(path):
    if not os.path.exists(path):
        os.makedirs(path)


def dir_delete(path):
    rmtree(path)


def hash_file(filepath):
    f = open(filepath)
    data = f.read()
    f.close()
    h = hashlib.sha256()
    h.update(data.encode('utf-8'))
    hash = h.hexdigest()
    return hash


def initialize():
    for dir in DIRS:
        dir_create(dir)


def system_check():
    assert sys.version_info >= MINIMUM_PYTHON_VERSION


def clone_repo(manifest_dict):
    dir_create(tempdir)
    for file in manifest_dict['reponames']:
        dir_create(tempdir + file)
        bash(f"cd {tempdir}{file}; git clone {manifest_dict['specs'][file]['spec']['repometadata']['urlbase']}/{file}.git")


def load_yaml_files(dirpath, repospecs):
    specs = []
    for repospec in repospecs:
        specs.append(yaml.load(open(dirpath + "/specs/" + repospec), Loader=yaml.Loader))
    return specs


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


def audit_repos(manifest_dict):
    for repo in manifest_dict["reponames"]:
        scan_for_requiredfiles_detailed(repo, manifest_dict["specs"][repo]['spec']['requiredfiles_detailed'])
        scan_for_requiredfiles_list(repo, manifest_dict["specs"][repo]['spec']['requiredfiles_list'])


def scan_for_repometadata():
    pass


def scan_for_requiredfiles_detailed(reponame, requiredfiles):
    for file in requiredfiles:
        filepath = tempdir + reponame + "/" + reponame + "/" + file['name']
        if os.path.exists(filepath):
            hash = hash_file(filepath)
            assert hash == file['hash']
            print("file ", filepath.replace(tempdir + reponame,""), " looks good")


def scan_for_requiredfiles_list(reponame, requiredfiles):
    for file in requiredfiles:
        filepath = tempdir + reponame + "/" + reponame + "/" + file
        if os.path.exists(filepath):
            print("file ", filepath.replace(tempdir + reponame,""), " exists")


def scan_for_similarfiles_detailed(reponame, requiredfiles):
    pass


def scan_for_similarfiles_list(reponame, requiredfiles):
    pass


def scan_for_requireddirs_detailed(reponame, requiredfiles):
    pass


def scan_for_requireddirs_list(reponame, requiredfiles):
    pass


def scan_for_forbiddenfiles_detailed(reponame, requiredfiles):
    pass


def scan_for_forbiddenfiles_list(reponame, requiredfiles):
    pass


def scan_for_requiredbranches_detailed(reponame, requiredfiles):
    pass


def scan_for_requiredbranches_list(reponame, requiredfiles):
    pass

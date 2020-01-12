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
    h.update(data.encode("utf-8"))
    hash = h.hexdigest()
    return hash


def initialize():
    for dir in DIRS:
        dir_create(dir)


def system_check():
    assert sys.version_info >= MINIMUM_PYTHON_VERSION


def clone_repo(manifest_dict):
    dir_create(tempdir)
    for file in manifest_dict["reponames"]:
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
            names = [line.split(" ")[0] for line in lines]
            names = [name.strip() for name in names]
            manifest_dict["reponames"] = names
            repospecs = [line.split(" ")[1] for line in lines]
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


def floating_decimals(f_val, dec):
    prc = "{:." + str(dec) + "f}"
    return prc.format(f_val)


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def printer(statements):
    statements[1] = (statements[1][:40] + '..') if len(statements[1]) > 40 else statements[1]
    print(f"{statements[0]:<20}  {statements[1]:<60}  {statements[2]:>20}")


def audit_repos(manifest_dict):
    for repo in manifest_dict["reponames"]:
        print("##########")
        print("##########")
        print("scanning", repo)
        print("repo size is:", floating_decimals(get_size(tempdir + repo + "/" + repo) / 1024 / 1024, 2), "mb")
        scan_for_requiredfiles_detailed(repo, manifest_dict["specs"][repo]["spec"]["requiredfiles_detailed"])
        scan_for_requiredfiles_list(repo, manifest_dict["specs"][repo]["spec"]["requiredfiles_list"])
        scan_for_forbiddenfiles_list(repo, manifest_dict["specs"][repo]["spec"]["forbiddenfiles_list"])
        scan_for_requireddirs_list(repo, manifest_dict["specs"][repo]["spec"]["requireddirs_list"])
        scan_for_requiredbranches_list(repo, manifest_dict["specs"][repo]["spec"]["requiredbranches_list"])


def scan_for_repometadata():
    pass


def scan_for_requiredfiles_detailed(reponame, requiredfiles):
    print("#####")
    print("scanning requiredfiles_detailed")
    for file in requiredfiles:
        filepath = tempdir + reponame + "/" + reponame + "/" + file["name"]
        if os.path.exists(filepath):
            hash = hash_file(filepath)
            assert hash == file["hash"]
            statements = ["file ", filepath.replace(tempdir + reponame, ""), "pass"]
            printer(statements)


def scan_for_requiredfiles_list(reponame, requiredfiles):
    print("#####")
    print("scanning requiredfiles_list")
    for file in requiredfiles:
        filepath = tempdir + reponame + "/" + reponame + "/" + file
        if os.path.exists(filepath):
            statements = ["file ", filepath.replace(tempdir + reponame, ""), "pass"]
            printer(statements)


def scan_for_similarfiles_detailed(reponame, requiredfiles):
    pass


def scan_for_similarfiles_list(reponame, requiredfiles):
    pass


def scan_for_requireddirs_detailed(reponame, requiredfiles):
    pass


def scan_for_requireddirs_list(reponame, requiredfiles):
    print("#####")
    print("scanning requireddirs_list")
    for dir in requiredfiles:
        dirpath = tempdir + reponame + "/" + reponame + "/" + dir
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            statements = ["dir", dirpath.replace(tempdir + reponame, ""), "pass"]
        else:
            statements = ["dir", dirpath.replace(tempdir + reponame, ""), "failed"]
        printer(statements)

def scan_for_forbiddenfiles_detailed(reponame, requiredfiles):
    pass


def scan_for_forbiddenfiles_list(reponame, requiredfiles):
    print("#####")
    print("scanning forbiddenfiles_list")
    for file in requiredfiles:
        filepath = tempdir + reponame + "/" + reponame + "/" + file
        if not os.path.exists(filepath):
            statements = ["file", filepath.replace(tempdir + reponame, ""), "pass"]
            printer(statements)


def scan_for_requiredbranches_detailed(reponame, requiredfiles):
    pass


def scan_for_requiredbranches_list(reponame, requiredbranches):
    print("#####")
    print("scanning requiredbranches_list")
    for branch in requiredbranches:
        branches = str(bash(f"cd {tempdir}{reponame}/{reponame}; git branch -a"))
        if branch in branches:
            statements = ["branch", branch, "pass"]
        else:
            statements = ["branch", branch, "fail"]
        printer(statements)

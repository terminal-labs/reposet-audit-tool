import os
import sys
import binascii
import pickle
import glob

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
    print(manifest_dict)


def load_manifest_dir(dirpath):
    manifest_dict = {}
    if os.path.isdir(dirpath): 
        files = os.listdir(dirpath)
        if "repos.txt" in files:
            f = open(dirpath + "/repos.txt", "r")
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            manifest_dict["reponames"] = lines
        return manifest_dict
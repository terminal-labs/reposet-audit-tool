import os
import sys
import binascii
import pickle
import glob

from repoaudittool.utils import create_dir
from repoaudittool.constants import HOURS_IN_WEEK
from repoaudittool.settings import *


def system_check():
    assert sys.version_info >= MINIMUM_PYTHON_VERSION


def initialize():
    for dir in DIRS:
        create_dir(dir)


def clone_repo(repo):
    pass

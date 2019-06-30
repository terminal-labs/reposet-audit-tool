import os
import binascii
import pickle
import glob

from utils import create_dir
from constants import HOURS_IN_WEEK
from settings import *


def initialize():
    for dir in DIRS:
        create_dir(dir)


def clone_repo(repo):
    pass

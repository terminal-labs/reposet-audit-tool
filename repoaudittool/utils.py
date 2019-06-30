import os

from settings import *


def read_file(fname):
    with open(fname, "rb") as f:
        content = f.read()
    return content


def write_file(data, path):
    with open(path, "wb") as the_file:
        the_file.write(data)


def create_dir(directroy):
    if not os.path.exists(directroy):
        os.makedirs(directroy)


def initialize():
    for dir in DIRS:
        create_dir(dir)

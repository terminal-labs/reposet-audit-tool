import os
import binascii
import pickle
import glob
from uuid import UUID

from repoaudittool.settings import *


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


def empty_dir(path):
    files = glob.glob(path + "/*")
    for f in files:
        if os.path.isfile(f):
            os.remove(f)


def stdio_print(data):
    if PRINT_VERBOSITY == "high":
        print(data)


def bytes_to_hex_str(data):
    data = pickle.dumps(data)
    data = binascii.b2a_hex(data)
    data = data.decode("utf-8")
    return data


def hex_str_to_bytes(data):
    data = binascii.a2b_hex(data)
    data = pickle.loads(data)
    return data


def validate_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False
    return val.hex == uuid_string.replace("-", "")


def ping(host):
    res = False

    ping_param = "-c 1"

    resultado = os.popen("ping " + ping_param + " " + host).read()

    if "ttl=" in resultado:
        res = True
    return res

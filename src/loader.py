import pathlib
from os.path import join, basename, abspath, isfile, dirname


def _import_fun(mod, func):
    return getattr(__import__(mod, fromlist=[func]), func)


def _get_pgk_name():
    def _cwd():
        return join(dirname(__file__))

    def _join(a, b):
        return abspath(join(a, b))

    currentpath = _cwd()
    i = len(currentpath.split("/"))
    while i > 0:
        currentpath = _join(currentpath, "..")
        if isfile(currentpath + "/setup.py"):
            return basename(currentpath).replace("-", "")
            i = -1
        i = i - 1

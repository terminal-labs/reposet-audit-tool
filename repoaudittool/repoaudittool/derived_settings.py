import os
import tempfile


def set_vars():
    APPDIR = os.path.abspath(os.path.dirname(__file__))
    SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
    TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
    MEMTEMPDIR = "/dev/shm"

    if os.path.isdir(MEMTEMPDIR):
        tempfile.tempdir = MEMTEMPDIR

    globals()["APPDIR"] = APPDIR
    globals()["SETUPFILEDIR"] = SETUPFILEDIR
    globals()["TESTDIR"] = TESTDIR
    globals()["MEMTEMPDIR"] = MEMTEMPDIR

    return {"APPDIR": APPDIR, "SETUPFILEDIR": SETUPFILEDIR, "TESTDIR": TESTDIR, "MEMTEMPDIR": MEMTEMPDIR}


set_vars()

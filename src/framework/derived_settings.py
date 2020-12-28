import os
import site
import tempfile

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

PACKAGENAME = _get_pgk_name()
PACKAGEDIR = _get_pgk_dir()
FRAMEWORKDIR = os.path.abspath(os.path.dirname(__file__))
SRCDIR = os.path.abspath(os.path.join(FRAMEWORKDIR, ".."))
APPDIR = os.path.abspath(os.path.join(FRAMEWORKDIR, ".."))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
MEMTEMPDIR = "/dev/shm"
SITEPACKAGESPATH = site.getsitepackages()[0]

if os.path.isdir(MEMTEMPDIR):
    tempfile.tempdir = MEMTEMPDIR

from repoaudittool.derived_settings import APPDIR, SETUPFILEDIR, TESTDIR, MEMTEMPDIR

VERSION = "0.0.3"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
PROJECT_NAME = "repoaudittool"
TEMPDIR = "/tmp"
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
DIRS = [f"{TEMPDIR}/repoauditworkingdirs", f"{TEMPDIR}/repoauditworkingdirs/repos"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

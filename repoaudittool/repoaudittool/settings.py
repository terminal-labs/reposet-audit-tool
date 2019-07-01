import os
VERSION = "0.1"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
TEMPDIR = "/tmp"
DIRS = [TEMPDIR + "/repoauditworkingdirs", TEMPDIR + "/repoauditworkingdirs/repos"]
MINIMUM_PYTHON_VERSION = (3,6,0)
APPDIR = os.path.abspath(os.path.abspath(os.path.dirname(__file__)))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, '..'))
TESTDIR = os.path.abspath(os.path.join(SETUPFILEDIR, 'repoaudittooltests'))

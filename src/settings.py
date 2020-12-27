import configparser

from repoaudittool.derived_settings import APPDIR, SETUPFILEDIR, TESTDIR, MEMTEMPDIR, SITEPACKAGESPATH
from repoaudittool.resolved_settings import get_env_variable, resolve_payload_path


config = configparser.ConfigParser()
config.read('setup.cfg')

VERSION = config["metadata"]["version"]
NAME = config["metadata"]["name"]

PROJECT_NAME = NAME
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
TEMPDIR = ".tmp/scratch"
DIRS = [f"{TEMPDIR}"]
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

# reponame = "code"
# VERSION = "0.0.1"
# PRINT_VERBOSITY = "high"
# EXCLUDED_DIRS = [".DS_Store"]
# SETUP_NAME = reponame
# PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
# EGG_NAME = SETUP_NAME.replace("_", "-")
# TEMPDIR = "/tmp"
# TEXTTABLE_STYLE = ["-", "|", "+", "-"]
# DIRS = [f"{TEMPDIR}/{SETUP_NAME}workingdirs"]
# MINIMUM_PYTHON_VERSION = (3, 6, 0)
# COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
# PAYLOADPATH = SITEPACKAGESPATH  # noqa: F841
# server_port = 5000
# socket_host = "0.0.0.0"
# PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
# )
# MONGO_DB = PROJECT_NAME  # noqa: F821
# UPLOAD_FOLDER = "uploads"
# ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
# STATIC_DIR = os.path.join(PAYLOADPATH, "static")
# PERSISTENT_WORKING_DIRS = "stub"
# CONFIG_DIC = {
#     "POSTGRES_URL": POSTGRES_URL,
#     "POSTGRES_USER": POSTGRES_USER,
#     "POSTGRES_PW": POSTGRES_PW,
#     "POSTGRES_DB": POSTGRES_DB,
# }
# tempfile.tempdir = TEMPDIR  # noqa: F821

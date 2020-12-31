import os
import sys

with open(os.path.dirname(__file__) + "/framework/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
MINIMUM_PYTHON_VERSION = _import_fun(f"{_pgk_name}.framework.settings", "MINIMUM_PYTHON_VERSION")
assert sys.version_info >= MINIMUM_PYTHON_VERSION

main = _import_fun(f"{_pgk_name}.cli", "main")
initialize = _import_fun(f"{_pgk_name}.core", "initialize")

initialize()
main()

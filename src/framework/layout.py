import os

with open(os.path.dirname(__file__) + "/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
PACKAGEDIR = _import_fun(f"{_pgk_name}.framework.derived_settings", "PACKAGEDIR")

APPDIR = _import_fun(f"{_pgk_name}.framework.settings", "APPDIR")
SETUPFILEDIR = _import_fun(f"{_pgk_name}.framework.settings", "SETUPFILEDIR")
MEMTEMPDIR = _import_fun(f"{_pgk_name}.framework.settings", "MEMTEMPDIR")
SITEPACKAGESPATH = _import_fun(f"{_pgk_name}.framework.settings", "SITEPACKAGESPATH")

def showlayout():
    return {
        "packagedir": PACKAGEDIR,
        "appdir": APPDIR,
        "setupfiledir": SETUPFILEDIR,
        "memtempdir": MEMTEMPDIR,
        "sitepackagepath":SITEPACKAGESPATH
    }

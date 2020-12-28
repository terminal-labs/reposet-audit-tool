import os

with open(os.path.dirname(__file__) + "/framework/loader.py") as f:
    code = compile(f.read(), "loader.py", "exec")
    exec(code)

_pgk_name = _get_pgk_name()
main = _import_fun(f"{_pgk_name}.cli", "main")
system_check = _import_fun(f"{_pgk_name}.app", "system_check")
initialize = _import_fun(f"{_pgk_name}.app", "initialize")

system_check()
initialize()
main()

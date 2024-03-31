# setup.py

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [],
    "include_files": ["assets"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("auto-click.py", base=base)
]

setup(
    name="autoSefaz-PI",
    version="3.0",
    description="Automação sefaz PI",
    options={"build_exe": build_exe_options},
    executables=executables
)

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [],
    "include_files": ["assets/"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Win32GUI" se você estiver criando uma GUI

setup(
    name="auto-sefaz-pi",
    version="2.0",
    description="Automatização de download de NF-e e NFC-e no site sefaz PI",
    options={"build_exe": build_exe_options},
    executables=[Executable("auto-click.py", base=base)],
)

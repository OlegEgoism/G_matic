from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("matic.py", base=base)]
icon_path = "icon.ico"
setup(
    name="G_matic",
    version="0.1",
    description="Learning mathematics",
    executables=executables,
    options={
        'build_exe': {
            'include_files': [(icon_path, 'icon.ico')],
        }
    }
)

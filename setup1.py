import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
##build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

includefiles = ['powerful-genre-218209-aec5a70ae8c1.json']

setup(  name = "GoogleSheetAPI_FirstStep",
        version = "0.1",
        description = "My google sheet API test application!",
        options = {"include_files": includefiles},
        executables = [Executable("GoogleSheetAPI_FirstStep.py", base=base)])

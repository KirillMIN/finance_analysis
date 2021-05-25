from cx_Freeze import setup, Executable

base = None

executables = [Executable("select_cat_mon.py", base=base)]

packages = ["idna", 'shelve','matplotlib.pyplot', 'PyQt5', 'sys']
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="<fin>",
    options=options,
    version="1.0",
    description='safe your money',
    executables=executables
)
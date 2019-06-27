from cx_Freeze import setup, Executable


base = None

executables = [Executable("main.py", base=base)]

packages = ["idna","pygame","sys","os","settings","sprites","tilemap","chest","construct","gold45","tilemap","wavax"] 
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "HatHome",
    options = options,
    version = "0.1",
    description = 'HatHome',
    executables = executables
)

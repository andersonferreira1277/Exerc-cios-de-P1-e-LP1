from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["os", "sys", "subprocess"], excludes = ["tkinter"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, targetName = 'declaracoes.exe')
]

setup(name='Gerador de Declarações',
      version = '0.1',
      description = 'Programas gerador de declarações',
      options = dict(build_exe = buildOptions),
      executables = executables)

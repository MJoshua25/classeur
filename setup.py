# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt5. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt5app.py is a very simple type of PyQt5 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'include_msvcr':True
    }
}
executables = [
    Executable('EDU-Classeur.py',
               base=base,
               icon="logo-Classuer.ico")
]

setup(name='EDU-Classeur',
      version='2.0',
      description='Gestionnaire de classe',
      options=options,
      executables=executables
      )

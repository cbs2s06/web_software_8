# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

# Include any necessary files
options = {
    'build_exe': {
        'include_files': [],
    }
}

# Set up the executable
exe = Executable(
    script='launcher.py',
    base='Win32GUI',
    icon='LOGO.ico',  
)

# Set up the setup function
setup(
    name='CBS2S06',
    version='1.0',
    description='AI「愛」在台灣新住民友誼之橋',
    options=options,
    executables=[exe],
)
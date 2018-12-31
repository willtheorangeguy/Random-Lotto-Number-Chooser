﻿"""
(C) 2016- 2019 William Vandergraaf and Mike McGrath. All rights reserved.
"""

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = { 'include_files' : ['lotto.gif'] , 'includes' : ['re'] }

setup(
    name = 'Lotto' ,
    version = '1.5' ,
    description = 'Lottery Number Picker' ,
    author = 'Mike McGrath' ,
    options = {'build_exe' : opts } ,
    executables = [ Executable( 'lotto.py' , base = base ) ] )

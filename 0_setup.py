#!/usr/bin/env python3
from sys import executable
from subprocess import call

# Install PyInquirer
try:
    import PyInquirer
except ImportError:
    call([executable, '-m', 'pip', 'install', 'PyInquirer'])

call([executable, '1_install_packages.py'])

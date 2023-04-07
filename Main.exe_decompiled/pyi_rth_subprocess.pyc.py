# Source Generated with Decompyle++
# File: pyi_rth_subprocess.pyc (Python 3.8)

import subprocess
import sys
import io

def Popen():
    '''Popen'''
    if not sys.platform == 'win32' and isinstance(sys.stdout, io.IOBase):
        
        def _get_handles(self = None, stdin = None, stdout = None, stderr = None):
            (stdin, stdout, stderr) = (lambda .0: for pipe in .0:
subprocess.DEVNULL if pipe is None else pipe)((stdin, stdout, stderr))
            return super()._get_handles(stdin, stdout, stderr)

    __classcell__ = None

Popen = <NODE:27>(Popen, 'Popen', subprocess.Popen)
subprocess.Popen = Popen

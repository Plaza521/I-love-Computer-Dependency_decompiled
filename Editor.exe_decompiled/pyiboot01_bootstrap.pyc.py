# Source Generated with Decompyle++
# File: pyiboot01_bootstrap.pyc (Python 3.8)

import sys
import pyimod02_importers
pyimod02_importers.install()
import os
if not hasattr(sys, 'frozen'):
    sys.frozen = True
sys.prefix = sys._MEIPASS
sys.exec_prefix = sys.prefix
sys.base_prefix = sys.prefix
sys.base_exec_prefix = sys.exec_prefix
VIRTENV = 'VIRTUAL_ENV'
if VIRTENV in os.environ:
    os.environ[VIRTENV] = ''
    del os.environ[VIRTENV]
python_path = []
for pth in sys.path:
    python_path.append(os.path.abspath(pth))
    sys.path = python_path

class NullWriter:
    softspace = 0
    encoding = 'UTF-8'
    
    def write(*args):
        pass

    
    def flush(*args):
        pass

    
    def isatty(self):
        return False


if sys.stdout is None:
    sys.stdout = NullWriter()
if sys.stderr is None:
    sys.stderr = NullWriter()

try:
    import encodings
finally:
    pass
except ImportError:
    pass


if sys.warnoptions:
    import warnings
import pyimod03_ctypes
pyimod03_ctypes.install()
d = 'eggs'
d = os.path.join(sys._MEIPASS, d)
if os.path.isdir(d):
    for fn in os.listdir(d):
        sys.path.append(os.path.join(d, fn))

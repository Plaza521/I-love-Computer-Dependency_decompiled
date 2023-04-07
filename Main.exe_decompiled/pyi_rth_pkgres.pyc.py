# Source Generated with Decompyle++
# File: pyi_rth_pkgres.pyc (Python 3.8)

import os
import pathlib
import sys
import pkg_resources
from pyimod02_importers import FrozenImporter
SYS_PREFIX = pathlib.PurePath(sys._MEIPASS)

class _TocFilesystem:
    '''
    A prefix tree implementation for embedded filesystem reconstruction.
    '''
    
    def __init__(self, toc_files, toc_dirs = (None,)):
        if not toc_dirs:
            pass
        toc_dirs = []
        self._tree = dict()
        for path in toc_files:
            path = pathlib.PurePath(path)
            current = self._tree
            for component in path.parts[:-1]:
                current = current.setdefault(component, { })
            current[path.parts[-1]] = ''
        for path in toc_dirs:
            path = pathlib.PurePath(path)
            current = self._tree
            for component in path.parts:
                current = current.setdefault(component, { })

    
    def _get_tree_node(self, path):
        path = pathlib.PurePath(path)
        current = self._tree
        for component in path.parts:
            if component not in current:
                return None
            current = None[component]
        return current

    
    def path_exists(self, path):
        node = self._get_tree_node(path)
        return node is not None

    
    def path_isdir(self, path):
        node = self._get_tree_node(path)
        if node is None:
            return False
        if None(node, str):
            return False

    
    def path_listdir(self, path):
        node = self._get_tree_node(path)
        if not isinstance(node, dict):
            return []
        return None(node.keys())


_toc_tree_cache = { }

def PyiFrozenProvider():
    '''PyiFrozenProvider'''
    __doc__ = '\n    Custom pkg_resources provider for FrozenImporter.\n    '
    
    def __init__(self = None, module = None):
        super().__init__(module)
        self._pkg_path = pathlib.PurePath(module.__file__).parent
        self._embedded_tree = None

    
    def _init_embedded_tree(self, rel_pkg_path, pkg_name):
        data_files = []
        package_dirs = []
    # WARNING: Decompyle incomplete

    
    def embedded_tree(self):
        if self._embedded_tree is None:
            rel_pkg_path = self._pkg_path.relative_to(SYS_PREFIX)
            pkg_name = '.'.join(rel_pkg_path.parts)
            if pkg_name not in _toc_tree_cache:
                _toc_tree_cache[pkg_name] = self._init_embedded_tree(rel_pkg_path, pkg_name)
            self._embedded_tree = _toc_tree_cache[pkg_name]
        return self._embedded_tree

    embedded_tree = property(embedded_tree)
    
    def _normalize_path(self, path):
        return pathlib.Path(os.path.abspath(path))

    
    def _is_relative_to_package(self, path):
        if not path == self._pkg_path:
            pass
        return self._pkg_path in path.parents

    
    def _has(self, path):
        path = self._normalize_path(path)
        if not self._is_relative_to_package(path):
            return False
        if None.exists():
            return True
        rel_path = None.relative_to(SYS_PREFIX)
        return self.embedded_tree.path_exists(rel_path)

    
    def _isdir(self, path):
        path = self._normalize_path(path)
        if not self._is_relative_to_package(path):
            return False
        rel_path = None.relative_to(SYS_PREFIX)
        node = self.embedded_tree._get_tree_node(rel_path)
        if node is None:
            return path.is_dir()
        return not None(node, str)

    
    def _listdir(self, path):
        path = self._normalize_path(path)
        if not self._is_relative_to_package(path):
            return []
        rel_path = None.relative_to(SYS_PREFIX)
        content = self.embedded_tree.path_listdir(rel_path)
        if path.is_dir():
            path = str(path)
            content = list(set(content + os.listdir(path)))
        return content

    __classcell__ = None

PyiFrozenProvider = <NODE:27>(PyiFrozenProvider, 'PyiFrozenProvider', pkg_resources.NullProvider)
pkg_resources.register_loader_type(FrozenImporter, PyiFrozenProvider)

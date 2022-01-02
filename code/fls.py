"""
FLS - File Load Save (simple wrappers for loading and saving data)

:fsave:     save data into a file
:fload:     load data from a file
"""
__VERSION__ = "1.0"
__DATE__ = "21/Sep/2021"

import os as _os
import gzip as _gzip

#########################################################
# # FSAVE/ FLOAD


def fsave(data, fn, path=None, binary=False, wrapper=None, quiet=False, compressed=False):
    """
    saves data to the file fn

    :data:          the data to be saved
    :fn:            the filename 
    :path:          the file path (default is "")
    :binary:        if the data is to be written as binary data
    :wrapper:       a wrapper string where `{}` is replaced with the data
    :quiet:         if True, do not print info message
    :compressed:    use gz compression (implies binary)
   """
    if not quiet: print (f"[fsave] Writing {fn} to {path}...")
    
    if not path is None:
        fn = _os.path.join(path, fn)
    
    if compressed: binary = True
    ftype = "wb" if binary else "w"

    if not wrapper is None:
        data = wrapper.format(data)
    
    if compressed:
        data = _gzip.compress(data.encode())

    with open (fn, ftype) as f:
        f.write(data)

def fload(fn, path=None, binary=False, wrapper=None, quiet=False, compressed=False):
    """
    loads data from the file fn

    :fn:            the filename 
    :path:          the file path (default is "")
    :binary:        if the data is to be written as binary data
    :wrapper:       a wrapper string where `{}` is replaced with the data
    :quiet:         if True, do not print info message
    :compressed:    use gz compression (implies binary)
    """
    if not quiet: print (f"[fload] Reading {fn}...")
    if not path is None:
        fn = _os.path.join(path, fn)

    if compressed: binary = True
    ftype = "rb" if binary else "r"
    with open (fn, ftype) as f:
        data = f.read()
    
    if compressed:
        data = _gzip.decompress(data)

    if not wrapper is None:
        data = wrapper.format(data)
    return data

CSSWRAPPER = "\n<style>\n{}\n</style>\n"


def join(*args):
    "convenience wrapper for os.path.join"
    return _os.path.join(*args)
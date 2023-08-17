#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/16 18:50
# @File     : utils.py
# @Desc     :
import os
import sys


def makepath(*paths):
    dir = os.path.join(*paths)
    try:
        dir = os.path.abspath(dir)
    except OSError:
        pass
    return dir, os.path.normcase(dir)


def abs_paths():
    """Set all module __file__ and __cached__ attributes to an absolute path"""
    for m in set(sys.modules.values()):
        if (getattr(getattr(m, '__loader__', None), '__module__', None) not in
                ('_frozen_importlib', '_frozen_importlib_external')):
            continue   # don't mess with a PEP 302-supplied __file__
        try:
            m.__file__ = os.path.abspath(m.__file__)
        except (AttributeError, OSError, TypeError):
            pass
        try:
            m.__cached__ = os.path.abspath(m.__cached__)
        except (AttributeError, OSError, TypeError):
            pass

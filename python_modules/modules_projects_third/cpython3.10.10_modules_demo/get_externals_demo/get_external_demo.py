#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/20 10:45
# @File     : get_external_demo.py
# @Desc     :

"""
Fetching external libraries...
Fetching sqlite-3.39.4.0...
Fetching xz-5.2.5...
Fetching zlib-1.2.13...
Fetching libffi-3.3.0...



Fetching的方式有两种， 一种是通过git拉取， 二是通过：python requests 请求 ， 显然这个失败， 是通过python请求的。
echo.Fetching %%e with git...
git clone https://github.com/python/cpython-bin-deps --branch  bzip2-1.0.8  externals/bzip2-1.0.8


https://github.com/python/cpython-bin-deps
https://github.com/python/cpython-source-deps

if "%ORG%"=="" (set ORG=python)
call "%PCBUILD%\find_python.bat" "%PYTHON%"
%PYTHON% -E "%PCBUILD%\get_external.py" -b -O %ORG% -e "%EXTERNALS_DIR%" %%b

https://github.com/python/cpython-bin-deps
https://github.com/python/cpython-source-deps

ORG
EXTERNALS_DIR
url = f'https://github.com/{org}/{repo}/archive/{commit_hash}.zip'
repo = f'cpython-{"bin" if binary else "source"}-deps'

'https://github.com/python/cpython-bin-deps/archive/sqlite-3.39.4.0.zip'
'D:\\aGitData\\cpython-3.10.10\\externals\\zip\\sqlite-3.39.4.0.zip'
"""



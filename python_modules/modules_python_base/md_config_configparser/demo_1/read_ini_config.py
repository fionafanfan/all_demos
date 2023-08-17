#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/17 14:32
# @File     : read_ini_config.py
# @Desc     :
import configparser

config = configparser.ConfigParser()
ret = config.sections()
print(ret)
config.read("example.ini")
ret = config.sections()
print(ret)

check = 'bitbucket.org' in config
print(check)

check = 'forge.example' in config
print(check)


user = config['forge.example']['User']
print(f"user:{user}")

compression = config['DEFAULT']['Compression']
print(f"compression:{compression}")

topsecret = config['topsecret.server.example']
print(topsecret, type(topsecret))
forwardx11 = topsecret['forwardx11']
print(f"forwardx11:{forwardx11}")

print("---------")
for key in config['topsecret.server.example']:
    print(key)

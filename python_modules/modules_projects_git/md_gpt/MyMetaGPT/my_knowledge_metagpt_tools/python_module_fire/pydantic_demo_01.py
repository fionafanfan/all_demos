#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/3/27 17:30
# @File     : pydantic_demo_01.py
# @Desc     :
from pydantic import BaseModel, Field


class Environment(BaseModel):
    roles: dict[str, Role] = Field(default_factory=dict)
    memory: Memory = Field(default_factory=Memory)
    history: str = Field(default='')
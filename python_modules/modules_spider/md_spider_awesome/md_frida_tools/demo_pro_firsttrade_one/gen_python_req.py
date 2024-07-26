#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/6/12 17:55
# @File     : gen_python_req.py
# @Desc     :
"""
500
The server encounter error, please contact our administrator for any enquiry.
"""
import requests

url = 'http://trade.firstsechk.com/i-trade/streaming/streamLogin'
data = 're=1&clm=NULnK0orswJGERdzxl5cpKn7eW0g4mk5lVWdlGIc7%2BRYNx%2FiJ8D7EnqPtiUL8gFkzaQn2GM4ot4x%0AJKE9%2Bi85pDLlEP1GvS2JjYFMlM6VeqzLhyufZYTvmE220V2Y8Mcz8T2llFBoPBkTe5h1tJXYcOCW%0AkgSgGbgfO8fbF2t51GgUKARz0vCNCGNDT3NCfo%2FenvFP5V%2BOlTJ3FTOw6TT%2B%2FfY8QGmJXgzajk77%0AAVOHqDGf7gVI2Tr6fJgG3E2QdP2RZseiJF5v3dEAr1yyR7bzbg8GlgKTQ1uJTorALnwtlRBy8UFC%0A1E%2FoWCqVd%2F33IFSjWFk1n4fsV7PEJdhLZfgkHylRTnI%2B6x0lRyz9%2BXmAz%2BarywGEjgTpWUjpiIea%0Ak4kScn7hPGlAv1fg7Agb4l88npx6SdoQiQ7vaUAwxsylIaEDMd9LHPorbY%2BNtTcCLoWlDIlMfJ1X%0AKhqgh5a8ZOgXKbv%2B7VLl3mSA579O2eDqtGaJRl%2BN%2BGxF3yMitF%2F2Q501x8yQ42oIg313xkT1R5uC%0AukFBhFVLUrx%2FXJ0lexTP3cVMDPiDCzqe3RC3y6fm4Xi47sipzb%2FN30zP9iXnQoPSK6bIMP3FKj9B%0A6w341Pm%2BN%2BL3eHWCIqkm1vIwKXA9wG6TO7VCEnuXjiOOV%2Fp%2FpKEEh9N2XoZcCB%2F%2BaPhfcR%2BdAF0%3D%0A'
ret = requests.post(url, data=data)
print(ret.status_code)
print(ret.text)
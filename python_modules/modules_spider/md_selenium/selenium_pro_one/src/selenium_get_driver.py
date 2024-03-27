#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/20 15:05
# @File     : selenium_get_driver.py
# @Desc     :
import requests


def get_url_for_version_and_platform(browser_version, platform):
    url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
    response = requests.get(url)
    data = response.json()
    versions = data["versions"]

    # 115及以上版本才会同时有chrome及chromediriver的下载链接
    # 该json文件chrome版本为113及113版本以上。
    # if version.parse(browser_version) >= version.parse("115"):
    if browser_version >= "115":
        short_version = ".".join(browser_version.split(".")[:3])
        compatible_versions = [v for v in versions if short_version in v["version"]]
        if compatible_versions:
            latest_version = compatible_versions[-1]
            print(f"WebDriver version {latest_version['version']} selected")
            downloads = latest_version["downloads"]["chromedriver"]
            for d in downloads:
                if d["platform"] == platform:
                    return d["url"]
    else:
        for v in versions:
            if v["version"] == browser_version:
                downloads = v["downloads"]["chromedriver"]
                for d in downloads:
                    if d["platform"] == platform:
                        return d["url"]

    raise Exception(f"No such driver version {browser_version} for {platform}")


url = get_url_for_version_and_platform("116", "win32")
# url = get_url_for_version_and_platform("114", "win32")
print(url)


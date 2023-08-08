#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/24 18:04
# @File     : test_parametrize.py
# @Desc     :
import pytest
import allure

cases = [("检查今开", "open"), ("检查昨收", "preClose"), ("检查最新价", "last"), ("检查最高价", "high")]


def case(title, stand_field):
    print(f"{title} {stand_field}")
    ret = [True, False]
    return ret


@allure.step("登录投管系统")
def login():
    print("登录投管系统成功")


@allure.step("请求A系统行情快照数据接口")
def get_a_celv_data():
    print("请求A系统行情快照数据接口成功")


@allure.step("请求B系统行情快照数据接口")
def get_b_celv_data():
    print("请求B系统行情快照数据接口成功")


@allure.step("数据比对")
def check_data():
    print("获数据比对成功")


@allure.step("获取视频附件")
def get_vedio():
    """
    语法：allure.attach.file(source, name, attachment_type, extension)，参数解释：
    source：文件路径，相当于传一个文件。
    name：附件名字。
    attachment_type：附件类型，是 allure.attachment_type 其中的一种。
    extension：附件的扩展名。
    :return:
    """
    print("获取视频附件")
    allure.attach.file(r'D:\aGitData\local_fiona_projects\all_demos\python_modules\modules_test\md_pytest\demo_1\attachments\自动化测试百度百科.mp4',
                       name="自动化测试视频讲解", attachment_type=allure.attachment_type.MP4, extension="mp4")


@allure.step("获取html附件")
def get_html():
    print("获取html附件")
    allure.attach.file(r'D:\aGitData\local_fiona_projects\all_demos\python_modules\modules_test\md_pytest\demo_1\attachments\attachment_test.html',
                       name="这是一个html附件", attachment_type=allure.attachment_type.HTML, extension="html")


@allure.step("获取图片附件")
def get_image():
    print("获取图片附件")
    allure.attach.file(r'D:\aGitData\local_fiona_projects\all_demos\python_modules\modules_test\md_pytest\demo_1\attachments\allure_how_works.png',
                       name="这是一个png图片附件", attachment_type=allure.attachment_type.PNG, extension="png")


@allure.step("获取csv附件")
def get_csv():
    print("获取csv附件")
    allure.attach.file(r'D:\aGitData\local_fiona_projects\all_demos\python_modules\modules_test\md_pytest\demo_1\attachments\csv_demo.csv',
                       name="这是一个csv附件", attachment_type=allure.attachment_type.CSV, extension="csv")


@allure.step("获取text附件")
def get_text():
    print("获取text附件")
    allure.attach.file(r'D:\aGitData\local_fiona_projects\all_demos\python_modules\modules_test\md_pytest\demo_1\attachments\txt_demo.txt',
                       name="这是一个text附件", attachment_type=allure.attachment_type.TEXT, extension="text")


# @allure.attachment_type()
@allure.epic("测试项目：投管系统")
@allure.feature("测试模块：行情")
@allure.story("美股行情指标测试")
@allure.severity("一般")
@allure.tag("一般关注")
@pytest.mark.parametrize("title,stand_field", cases)
class TestParam:

    @allure.title("检查美股行情字段")  # 用例标题
    def test_case(self, title, stand_field):
        print(f"测试函数case的数据: title={title}, stand_field={stand_field}")
        assert all(case(title, stand_field)), f"【{title}】不通过"


@allure.epic("测试项目：allure报告")
@allure.feature("测试模块：allure报告定制")
@allure.story("allure报告")
@allure.severity("一般")
@allure.tag("一般关注")
@allure.description("类描述")
class TestAllure:

    @allure.title("allure报告-测试步骤")  # 用例标题
    def test_step(self):
        login()
        get_a_celv_data()
        get_b_celv_data()
        check_data()
        ret = False
        assert ret, "不通过"

    @allure.title("测试allure报告的附件添加")
    @allure.description("方法描述2")
    def test_allure_attach(self):
        """
    TEXT = ("text/plain", "txt")
    CSV = ("text/csv", "csv")  # ok
    TSV = ("text/tab-separated-values", "tsv")
    URI_LIST = ("text/uri-list", "uri")

    HTML = ("text/html", "html")  # ok
    XML = ("application/xml", "xml")
    JSON = ("application/json", "json")
    YAML = ("application/yaml", "yaml")
    PCAP = ("application/vnd.tcpdump.pcap", "pcap")

    PNG = ("image/png", "png")  # ok
    JPG = ("image/jpg", "jpg")
    SVG = ("image/svg-xml", "svg")
    GIF = ("image/gif", "gif")
    BMP = ("image/bmp", "bmp")
    TIFF = ("image/tiff", "tiff")

    MP4 = ("video/mp4", "mp4")  # ok
    OGG = ("video/ogg", "ogg")
    WEBM = ("video/webm", "webm")

    PDF = ("application/pdf", "pdf")
        :return:
        """
        get_vedio()
        get_html()
        get_image()
        get_csv()
        get_text()




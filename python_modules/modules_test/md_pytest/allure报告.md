# allure报告
Allure Report优秀的的报告解决方案

官方链接：https://qameta.io/allure-report/
截至2023/8/7，官网链接上标记的最新版本是2.21.0版本
而github仓库地址： https://github.com/allure-framework/allure2/releases
可以下载到2.23.1版本， 而我在7月25号左右使用的是2.23.0版本  


| allure报告支持的                                                     |
|--------------------------------------------------------------|
| 从带有通过、失败或跳过结果的测试用例附件的报告中获取更多细节。                              |
| 聚合Web, API，桌面或移动测试结果(或不!):Allure支持所有这些。                      |
| Allure支持嵌套步骤，以便在报告中提供清晰的测试数据展示。                              |
| 灵活的基于树的测试用例表示允许您根据许多属性搜索、过滤和分组测试用例。                          |
| Allure不支持您的测试框架?自己进行集成:提供了指南和文档。如果您需要任何帮助，请随时在GitHub讨论中提出问题。 |
| 使用强大的导出引擎自定义视图，使您可以创建出色的HTML报告。                              |
| 您可以随意使用漂亮且稳定的API和句柄系统来定制您的报表。                                |

## allure报告的定制
Allure用例描述
```angular2html
使用方法	参数值	参数说明
@allure.epic()	epic描述	定义项目、当有多个项目是使用。往下是feature
@allure.feature()	模块名称	用例按照模块区分，有多个模块时给每个起名字　　
@allure.story()	用例名称	一个用例的描述
@allure.title(用例的标题)	用例标题	一个用例标题
@allure.testcase()	测试用例的连接地址	自动化用例对应的功能用例存放系统的地址
@allure.issue()	缺陷地址	对应缺陷管理系统里边的缺陷地址
@allure.description()	用例描述	对测试用例的详细描述
@allure.step()	操作步骤	测试用例的操作步骤
@allure.severity()	用例等级	blocker  、critical  、normal  、minor  、trivial
@allure.link()	定义连接	用于定义一个需要在测试报告中展示的连接
@allure.attachment()	附件	添加测试报告附件
```

allure测试报告附件类型:
```cython
"""
class AttachmentType(Enum):

    def __init__(self, mime_type, extension):
        self.mime_type = mime_type
        self.extension = extension

    TEXT = ("text/plain", "txt")
    CSV = ("text/csv", "csv")
    TSV = ("text/tab-separated-values", "tsv")
    URI_LIST = ("text/uri-list", "uri")

    HTML = ("text/html", "html")
    XML = ("application/xml", "xml")
    JSON = ("application/json", "json")
    YAML = ("application/yaml", "yaml")
    PCAP = ("application/vnd.tcpdump.pcap", "pcap")

    PNG = ("image/png", "png")
    JPG = ("image/jpg", "jpg")
    SVG = ("image/svg-xml", "svg")
    GIF = ("image/gif", "gif")
    BMP = ("image/bmp", "bmp")
    TIFF = ("image/tiff", "tiff")

    MP4 = ("video/mp4", "mp4")
    OGG = ("video/ogg", "ogg")
    WEBM = ("video/webm", "webm")

    PDF = ("application/pdf", "pdf")
"""
```


## allure报告的logo定制， 替换为自己的logo及文字

找到自己电脑安装allure的位置， 打开config路径： D:\Tools_an\allure-2.23.0\config
修改该目录下的allure.yml文件, 在末尾添加:- custom-logo-plugin; 保存。
```angular2html
plugins:
  - junit-xml-plugin
  - xunit-xml-plugin
  - trx-plugin
  - behaviors-plugin
  - packages-plugin
  - screen-diff-plugin
  - xctest-plugin
  - jira-plugin
  - xray-plugin
  - custom-logo-plugin
```

进入目录： D:\Tools_an\allure-2.23.0\plugins\custom-logo-plugin\static
将自己的.png的logo放到该路径下
修改styles.css ， 通过写样式让自己的logo和页面完美融合， 大功告成， 样式参考如下：
```angular2html
.side-nav {
    background: #041529;  // 侧边栏的颜色
}
.side-nav__brand {
  background: url('my_logo.png') no-repeat left center !important;
    margin-left: 10px;
  height: 40px;
  background-size: contain !important;
}

.side-nav__brand span{
	display: none;
}

.side-nav__brand:after{
	content: "my_title";
	margin-left: 20px;

}
```

存在问题：
content: "标题"; 如果content内容为中文，会显示乱码
content: "my_title"; 字符串长度不能超过一定数据， 否则会换行
margin-left: 20px;  如果20px 再调大一点，整个界面会变为只有数据的版面，而不是报告显示页面
样式，需要再根据自己的想法设计恰当调整。
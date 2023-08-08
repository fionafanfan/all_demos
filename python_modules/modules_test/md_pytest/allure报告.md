# allure����
Allure Report����ĵı���������

�ٷ����ӣ�https://qameta.io/allure-report/
����2023/8/7�����������ϱ�ǵ����°汾��2.21.0�汾
��github�ֿ��ַ�� https://github.com/allure-framework/allure2/releases
�������ص�2.23.1�汾�� ������7��25������ʹ�õ���2.23.0�汾  


| allure����֧�ֵ�                                                     |
|--------------------------------------------------------------|
| �Ӵ���ͨ����ʧ�ܻ���������Ĳ������������ı����л�ȡ����ϸ�ڡ�                              |
| �ۺ�Web, API��������ƶ����Խ��(��!):Allure֧��������Щ��                      |
| Allure֧��Ƕ�ײ��裬�Ա��ڱ������ṩ�����Ĳ�������չʾ��                              |
| ���Ļ������Ĳ���������ʾ��������������������������˺ͷ������������                          |
| Allure��֧�����Ĳ��Կ��?�Լ����м���:�ṩ��ָ�Ϻ��ĵ����������Ҫ�κΰ���������ʱ��GitHub������������⡣ |
| ʹ��ǿ��ĵ��������Զ�����ͼ��ʹ�����Դ�����ɫ��HTML���档                              |
| ����������ʹ��Ư�����ȶ���API�;��ϵͳ���������ı���                                |

## allure����Ķ���
Allure��������
```angular2html
ʹ�÷���	����ֵ	����˵��
@allure.epic()	epic����	������Ŀ�����ж����Ŀ��ʹ�á�������feature
@allure.feature()	ģ������	��������ģ�����֣��ж��ģ��ʱ��ÿ�������֡���
@allure.story()	��������	һ������������
@allure.title(�����ı���)	��������	һ����������
@allure.testcase()	�������������ӵ�ַ	�Զ���������Ӧ�Ĺ����������ϵͳ�ĵ�ַ
@allure.issue()	ȱ�ݵ�ַ	��Ӧȱ�ݹ���ϵͳ��ߵ�ȱ�ݵ�ַ
@allure.description()	��������	�Բ�����������ϸ����
@allure.step()	��������	���������Ĳ�������
@allure.severity()	�����ȼ�	blocker  ��critical  ��normal  ��minor  ��trivial
@allure.link()	��������	���ڶ���һ����Ҫ�ڲ��Ա�����չʾ������
@allure.attachment()	����	��Ӳ��Ա��渽��
```

allure���Ա��渽������:
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


## allure�����logo���ƣ� �滻Ϊ�Լ���logo������

�ҵ��Լ����԰�װallure��λ�ã� ��config·���� D:\Tools_an\allure-2.23.0\config
�޸ĸ�Ŀ¼�µ�allure.yml�ļ�, ��ĩβ���:- custom-logo-plugin; ���档
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

����Ŀ¼�� D:\Tools_an\allure-2.23.0\plugins\custom-logo-plugin\static
���Լ���.png��logo�ŵ���·����
�޸�styles.css �� ͨ��д��ʽ���Լ���logo��ҳ�������ںϣ� �󹦸�ɣ� ��ʽ�ο����£�
```angular2html
.side-nav {
    background: #041529;  // ���������ɫ
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

�������⣺
content: "����"; ���content����Ϊ���ģ�����ʾ����
content: "my_title"; �ַ������Ȳ��ܳ���һ�����ݣ� ����ỻ��
margin-left: 20px;  ���20px �ٵ���һ�㣬����������Ϊֻ�����ݵİ��棬�����Ǳ�����ʾҳ��
��ʽ����Ҫ�ٸ����Լ����뷨���ǡ��������
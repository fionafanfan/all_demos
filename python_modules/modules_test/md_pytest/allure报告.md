# allure����

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
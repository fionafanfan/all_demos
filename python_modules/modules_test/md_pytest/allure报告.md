# allure报告

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
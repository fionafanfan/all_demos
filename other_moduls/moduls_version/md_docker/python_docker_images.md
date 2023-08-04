# docker python镜像

版本号:
buster(适用于debian 10)
stretch(适用于debian 9)
jessie(适用于debian 8)
bullseye、bookworm (开发版本，处于未稳定状态)

slim: 表示最小安装包， 仅包含需要运行指定容器的特定工具集
使用slim版本时， 一定要进行完全测试， 若功能无法满足要求就要更换完整版镜像

apphine专门为容器构建的操作系统， 比其的操作系统更小， 但是会缺少很多软件包并且是哦给你glibc等都是阉割版

windows server：适配window和windows server的容器 



centos 安装 selenium / ChromeDriver / chrome
https://juejin.cn/post/6844903752483209224

alpine 安装 selenium / ChromeDriver / chrome

https://blog.csdn.net/zyy247796143/article/details/123266186(亲测有用)
https://www.jianshu.com/p/009ff8ba87ba(亲测有用，差不多)


fc-list :lang=zh 查看字体（查看有用）

chromium-browser --version 查看chrome版本 （查看有用）

chromedriver --version 查看驱动版本（查看有用）

python --version 查看python版本（查看有用）

pip list 查看python模块版本（查看有用）

apk --version apk包管理工具（查看有用）

selenium-grid
selenium爬虫chrome容器化部署实战:
https://blog.csdn.net/jgku/article/details/127548990  (最终使用方案)

--restart always
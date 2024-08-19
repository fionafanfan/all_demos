# all demos 所有demo示例

项目结构
- python_modules【模块及框架】
  - modules_test【测试】
    - md_pytest
    - md_unitest
    
  - modules_gui【桌面GUI】
    - md_tkinter
    - md_pyqt5
    - md_wxpython
    
  - modules_web【web框架】
    - md_tornado
    - md_flask
    - md_django
    
  - modules_database【数据库客户端】
    - md_mysql_pymysql
    - md_redis_redis
    - md_kafka_kafka
    - md_es_es
    - md_mongo_pymongo
  
  - modules_other【其他】
    - 暂无
  
在执行某些demo时，可以单独构建自己的虚拟环境：
譬如：
- conda create -n all_demos_py36 python==3.6
- conda create -n all_demos_py37 python==3.7
- conda create -n all_demos_py3_10 python==3.10
- conda create -n all_demos_py37_md_pytest python==3.7
- conda create -n cpython31010_demo python==3.10
激活环境： conda activate all_demos_py36

然后在新建的虚拟环境中， 安装对应的依赖包： pip install -r requirements.txt -i https://pypi.douban.com/simple/

其它源：
清华大学 ：https://pypi.tuna.tsinghua.edu.cn/simple/

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科学技术大学 ：http://pypi.mirrors.ustc.edu.cn/simple/

华中科技大学：http://pypi.hustunique.com/

豆瓣源：http://pypi.douban.com/simple/

腾讯源：http://mirrors.cloud.tencent.com/pypi/simple

华为镜像源：https://repo.huaweicloud.com/repository/pypi/simple/

     
  
  
  


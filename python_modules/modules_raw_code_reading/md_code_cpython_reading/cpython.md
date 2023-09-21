# cpythonԴ����

## ��ȡcpythonԴ��
* git clone https://github.com/python/cpython
* githubѡ��ָ��python�汾����.zip�ļ������ؽ��н�ѹ, �磺 https://github.com/python/cpython/tree/v3.10.10

## cpythonԴ��ṹ
![img_1.png](cpythonԴ��ṹ.png)
```text
cpython/
��
������ Doc �� Դ�����ĵ�˵��
������ Grammar �� ������ɶ������Զ���
������ Include �� C ����ͷ�ļ���ͷ�ļ���һ���һЩ�ظ�ʹ�õĴ��룩
������ Lib �� Python д�ı�׼���ļ�
������ Mac �� Mac ֧�ֵ��ļ�
������ Misc �� ����
������ Modules �� C д�ı�׼���ļ�
������ Objects �� �������ͺͶ���ģ��
������ Parser �� Python ������Դ��
������ PC �� Windows ����֧�ֵ��ļ�
������ PCbuild �� �ϰ汾�� Windows ϵͳ ����֧�ֵ��ļ�
������ Programs �� Python ��ִ���ļ��������������ļ���Դ����
������ Python �� CPython ������Դ��
������ Tools �� ���ڹ�������չ Python �Ķ�������
```

��׼��: Lib + Modules
python����������:Python + Parser + Objects + Includes
�ĵ���أ� Doc + Grammar
ƽ̨���빤�����: Mac + Misc + PC + PCbuild + programes + Tools 


* Parser��  ��pythonԴ�� ����Ϊ ast�����﷨��
  * �ʷ������� tokenizer (�ʷ�����������Դ����ֽ�Ϊһϵ�дʷ���Ԫ��tokens����������ʶ�����ؼ��֡�������������ȡ��ʷ���������ʵ�ֿ����� Parser/tokenizer.c �ļ����ҵ�����Щ tokens �ᱻ���ݸ��﷨�������Թ����﷨����)
  * �﷨������ parser (�﷨��������parser�����ܴʷ����������ɵ� tokens������������֯���﷨����AST����Python ���������﷨��������ʵ�ִ���λ�� Parser/parser.c �ļ��С��﷨������ʹ�� Python �﷨���򣨶����� Grammar/Grammar �ļ��У���ȷ������Ľṹ��)
  * ����Ͳ��������﷨���Ĵ��� AST (�﷨�����������ɳ����﷨����AST�������Ǵ���ĳ����ʾ�����ڱ�ʾ����Ľṹ�����塣AST �Ľڵ����ͬ���﷨�ṹ�����纯�����á���ֵ���������ȡ�AST ͨ�������ڴ���������Ż���ִ�С�Python ������ͨ�������﷨�������� AST ������������Դ�������Ϊ AST��һ�� AST ������ɣ����������Զ� AST ���н�һ���Ĵ����ִ�С�)

* ��ʶcpython��Դ��ṹ ��ok��
* �ɹ�����cpython��Դ�� ��windows��linux��mac  һ����û���Թ���
* ΪPythonдc��չ

-----
PCbuild�е�bat�ű���

![img.png](cpython_pcbuild_bat_list.png)

����˵����Դ���е��ĵ�˵����
* cpython-3.10.10/PCbuild/readme.txt 
* cpython-3.10.10/Tools/msi/README.txt


������ڣ�Դ���еı���·�ڣ�
* cpython-3.10.10/PCbuild/build.bat (��win11ϵͳ����ɹ��� �ҿ���������pycharm����ʹ��)
* cpython-3.10.10/Tools/msi/build.bat
* cpython-3.10.10/Tools/msi/buildrelease.bat


����cpython���ݹ���ָ���ĵ���chatgpt��ʾ��
1.ִ�� PCbuild�е�build.bat�ű��ļ� (��������������б��� �����鿴��־����֪���ǻ�ȡexternals�����ļ��������º�����뱨��
����������У� ����ִ��build.bat�ű� ��ȡexternals�ļ�����ʵ��������get_externals.bat���� get_external.py�ļ�)
(bat�ű�����)
build.bat(�ű��ڵı�ǩ�ڵ�):
1. :Usage
2. :Run
3. :CheckOpts
4. :Kill
5. :Build
6. :Regen
7. :Build
8. :Version

build.bat(ִ��˳��):
goto Run
goto :Build
�ҵ�msbuild.



1. build.bat --> get_externals.bat --> externals
2. build.bat --> find_msbuild.bat -- > MSBUILD
3. build.bat --> find_python.bat --> PYTHON
4. get_externals.bat --> get_external.py �����Ե������ã� ����������ʱ����������ᱨ�������Ӵ��� �ҵ���û���޸Ķ����� ֻ�Ƕೢ���˺ö�Σ��Ű���Ҫ�İ����������ˣ�
5. get_external.py --> org --> find_python.bat

���⣺
û�б���tkinter, ���޷�ʹ��tkinterģ��

![img.png](img.png)
-----
�ο������۽��飺
* cpy��Դ�룬�����е㸴�ӵģ���ʵ��չ��Ϊ��������Ե�Դ�붼�Ƚϸ��ӣ�����˵�Ѷ��ж�ߣ������ݶ���ģ��������Щ��ϣ�����Щtrick����ѧ�ߵĻ�������һЩ�򵥵�DSLʵ���ȿ����������һЩ����ԭ��ʵ��������������Ч�ʻ����Щ
* chatgpt�ʴ� + ʵ��

�ο����ϣ�
1. https://github.com/shishujuan/python-source-code-analysis(������߽�����python�汾2.5.6��ԭ����д�����������������Ǹ��汾һ�£��汾��2.5.6.Դ�����������)
2. https://github.com/hitlic/python_book ��python�Ļ�����ѧ�γ̣�
3. https://www.bilibili.com/video/BV1sS4y1g7hN/?spm_id_from=333.337.search-card.all.click&vd_source=9ab8a945335cbaf24c13e51eba88b195 (bվ������ Cpyhon��Cython������)
4. https://www.zhihu.com/tardis/bd/art/210849122?source_id=1001 ����һ��Cython����
5. https://www.applenice.net/2020/06/21/Build-CPython-on-Windows/ ������cpython�ο����£� ��ʵ������ ����pcbuild.sln��vstudio�������õ���
6. https://www.cnblogs.com/np10/p/5185477.html (��Ȼ��ƪ�Ľ���2.x�汾��cpython���룬�������п��Խ���ĵط��� pcbuild.sln����ʱ�� ���Կ������ɾ��������Ҫ�Ŀ⣬��������ɹ���ɾ���Ŀ�Ͳ���Ҫ��)
7. https://blog.csdn.net/deflypig/article/details/121448926 (MSBuild���� csdn����)
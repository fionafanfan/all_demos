# 反编译

问题：
1. exe文件有办法查到用的什么后端语言编写的吗： https://exe.yimenapp.com/info@-exe-cha-kan-kai-fa-yu-yan-51358.html
2. 查壳工具PEiD（可以下载试用）： https://www.aldeid.com/wiki/PEiD
3. exeinfo: https://exeinfo.orgfree.com/index.htm
https://zhuanlan.zhihu.com/p/649826303
https://exeinfo.orgfree.com/index.htm
https://github.com/ExeinfoASL/ASL/blob/master/exeinfope.zip
3. 脱壳： https://baike.baidu.com/item/%E8%84%B1%E5%A3%B3/9482636?fr=ge_ala
4. 侦测壳： 侦测壳和软件所用编写语言的软件，因为脱壳之前要查他的壳的类型(1、侦测壳的软件fileinfo.exe，简称fi.exe（侦测壳的能力极强）；2.侦测壳和软件所用编写语言的软件language.exe（两个功能合为一体，很棒），推荐language2000中文版（专门检测加壳类型）；3.软件常用编写语言Delphi，VisualBasic（VB）。)
```text
1、文件分析工具（侦测壳的类型）：Fi，GetTyp，peid，pe-scan，
2、OEP入口查找工具：SoftICE，TRW，ollydbg，loader，peid
3、dump工具：IceDump，TRW，PEditor，ProcDump32，LordPE
4、PE文件编辑工具PEditor，ProcDump32，LordPE
5、重建Import Table工具：ImportREC，ReVirgin
6、ASProtect脱壳专用工具：Caspr（ASPr V1.1-V1.2有效），Rad（只对ASPr V1.1有效），loader，peid（1）Aspack：用的最多，但只要用UNASPACK或PEDUMP32脱壳就行了
```
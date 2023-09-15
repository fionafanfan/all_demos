# python官方文档

3.10版本（num onece):
https://docs.python.org/zh-cn/3.10/library/index.html

语言核心
* 数据类型

python组件：
* 单独的程序
* 模块
* 软件包
* 应用开发框架

python组件分类：
* 系统级功能
  * 文件I/O
* 日常编程中许多问题的标准解决方案


Python 库应该有所了解的：
* python 库的可用模块
* Python 库所支持的应用领域 


python模块的类别：
* 用C编写并内置于python解释器中（内置函数对象是对于 C 函数的外部封装）
* 用python编写并以源码形式导入
* 提供专用于python的接口， 例如：打印栈追踪信息
* 提供专用于特定操作系统的接口， 例如：操作特定的硬件
* 针对特定领域的接口， 例如：万维网

python模块的使用范围：
* 有些模块在所有更新和移植版本的 Python 中可用
* 另一些模块仅在底层系统支持或要求时可用
* 还有些模块则仅当编译和安装 Python 时选择了特定配置选项时才可用

官方文档介绍python库的顺序是：
* 内置行数（无论你想以怎样的顺序阅读本手册，还是建议先从 内置函数 这一章开始，因为本手册的其余内容都需要你熟悉其中的基本概念）
* 数据类型
* 异常
* 按照相关性分类介绍各组别的各种模块

Ps： python文档几乎是一个模块或者一个库就占一页内容。 

python内置函数的几个大类别：
--------

数据类型相关:
  1. bool()
  2. bytes()     字节串 是 不可变的数组  通过 decode() 解码为 字符串
  3. bytearray()   字节数组 是 可变数组； 扩展模块, array模块与 collections模块 提供了一个额外可变序列类型示例
  4. complex()
  5. dict()  提供了额外的映射类型示例： 扩展模块 dbm.ndbm 和 dbm.gnu ； collections模块
  6. float()
  7. frozentset()
  8. hash()
  9. list()
  10. int()
  11. set()
  12. str()
  13. tuple()
  14. memoryview()

进制相关:
  1. bin()  二进制  bin(6)  返回： 0b110
  2. oct()  八进制  oct(8)  返回： 0o10
  3. hex()  十六进制  hex(16)  返回： 0x10

数学计算相关
  1. abs()  绝对值 abs(-1)  返回： 1
  2. divmod()  除余  divmod(10, 3) 返回： (3, 1)
  3. max()      最大值  max([1, 3, 5, 7])  返回： 7
  4. min()      最小值   min([1, 3, 5, 7]) 返回： 1
  5. pow()      次方    pow(3, 3)  返回： 27
  6. round()    四舍五入 round(1.35, 2)  返回： 1.35  (算是四舍六入， 不算真正意义上的四舍五入)
  7. sum()      和   sum([1, 2, 3])  返回： 6

python争对数据类型的一些属性计算：
1. len()
2. slice()

python高阶函数相关：
1. all()
2. any()
3. enumerate()
4. filter()
5. map()
6. range()
7. reversed()
8. sorted()
9. zip()


python迭代器生成器相关的：
1. aiter()
2. anext()
3. iter()
4. next()

python属性相关：
1. delattr()
2. getattr()
3. setattr()
4. property()
5. staticmethod()
6. classmethod()

python变量区间相关：
1. globals()
2. locals()

python内省相关：
1. isinstance()
2. issubclass()
3. type()
4. id()
5. help()
6. callable()
7. object()

python字符相关：
1. ascii()
2. chr()
3. ord()

io相关：
1. input()
2. print()
3. format()
4. open()

3.7版本中新加的几个内置函数：
1. breakpoint()

3.10版本新增加了几个内置函数：
1. aiter()   内置函数iter()的异步版本
2. anext()   内置函数next()的异步版本

标准类型层级结构？


感兴趣的模块：
* 配置文件解析器-configparser
* 关于测试方向
  * doctest
  * unittest
  * test  python回归测试包

ini配置文件：
* ini文件的结构， 由多个节组成
* 每个节包含多个带有值的键


configparser：
* configparser类可以读取和写入这种文件
* 可以把配置解析器当作一个字典来处理， 但是又和字典有区别
* 值的插入， 变量替换 ， 可以在同一个小节中，  也可以跨小节

阅读python.org收获：
faq问题：
* python常见问题
* 编程常见问题
* 设计和历史常见问题
* 代码库和插件常见问题
* 扩展和嵌入常见问题


编程常见问题：
* 全局变量与局部变量
* 如何跨模块共享全局变量？
（确实都是这样实践的，哈哈：在单个程序中跨模块共享信息的规范方法是创建一个特殊模块（通常称为 config 或 cfg）。只需在应用程序的所有模块中导入该 config 模块；然后该模块就可当作全局名称使用了。因为每个模块只有一个实例，所以对该模块对象所做的任何更改将会在所有地方得以体现。）
* 为什么对象之间会共享默认值？ mydict函数默认值只会在定义的时执行一遍。
* 如何编写带有输出参数的函数（按照引用调用）？
* 如何在 Python 中创建高阶函数？
  * 嵌套作用域
  * 可调用对象

设计和历史常见问题：

代码库和插件常见问题(可以重复看看)：
* math.py (socket.py regex.py等) 的源文件在哪里？
```text
Python 中（至少）有三类模块：

使用 Python 编写的模块（.py)；

使用 C 编写的动态加载模块（.dll，.pyd，.so，.sl 等）；

使用 C 编写并链接到解释器的模块，要获取此列表，输入(已测试过):
import sys
print(sys.builtin_module_names) 
```
扩展/嵌入常见问题：



sys模块阅读：

动态变量：
静态变量：
比较有记忆点的变量(源码原文注释：variables with complex values)：
sys.orig_argv：传给 Python 可执行文件的原始命令行参数列表。
sys.path:是一个由路径字符串组成的列表， 可以通过site模块使用.pth文件来扩展sys.path（还没有进行实践过）

函数：

观察sys.py源码， 可以通过idea看到下面一些注释， 可以弄清楚这些含义。
# real signature unknown
# real signature unknown; restored from __doc__
# real signature unknown; NOTE: unreliably restored from __doc__ 
# reliably restored by inspect : 是指使用inspect模块可以可靠地恢复函数定义

sys模块中的函数真正的实现都是用c语言实现的， 没有python源码，而sys.py模块中只是用一个空方法占位而已。
这个函数的具体实现不用python编写，而是由例如C这种高效语法编写，在包中只用一个空方法占位，调用的时候是调用C语言实现的方法
(有些附带注释的接口是提供给用户看的，告诉用户如何使用，有的函数的实现代码你是看不到的，你最多看到一些接口说明。
是ide为了提供友好提示而搞的
)



































































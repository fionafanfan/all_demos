# python库

1. idlelib： 是纯python写的， 界面由tkinter写的
2. tkinter: 看源码是written by Fredrik Lundh, May 1997



tkinter源码:

* Binary Skeletons
  * _tkinter.py 
    * Values
      * ALL_EVENTS
      * DONT_WAIT
      * EXCEPTION
      * FILE_EVENTS
      * IDLE_EVENTS
      * READABLE
      * TCL_VERSION
      * TIMER_EVENTS
      * TK_VERSION
      * WINDOW_EVENTS
      * WRITABLE
    * Functions
      * create
      * getbusywaitinterval
      * setbusywaitinterval
      * _flatten
    * classes
      * TclError
      * Tcl_Obj
      * TkappType
      * TkttType
* cpython-3.10.10/Modules/clinic/_tkinter.c.h
* cpython-3.10.10/Modules/_tkinter.c
  * ctype.h
  * windows.h
  * cpython-3.10.10/Modules/Python.h
  * cpython-3.10.10/Modules/tkinter.h
  * Tcl/tcl.h
  * Tk/tk.h
  * tcl.h
  * tk.h
  * tclTomMath.h
  * conio.h
    * cpython-3.10.10/Modules/_tkappinit.c
      * string.h 
      * tcl.h
      * tk.h
      * cpython-3.10.10/Modules/tkinter.h
        * cpython-3.10.10/Lib/tkinter
          * __init__.py 
            * _tkinter.py 等同于 _tkinter.c ， 所以来的常量、方法、类 都在编译的时候固定了，都是占位起到提示作用，真正的实现都是在c中实现。
              * _tkinter.TclError
              * _tkinter.TK_VERSION
              * _tkinter.TCL_VERSION
              * _tkinter.READABLE
              * _tkinter.WRITABLE
              * _tkinter.EXCEPTION
              * _tkinter._flatten
              * _tkinter._cnfmerge
              * _tkinter.Tcl_Obj
              * _tkinter.create 
                * _tkinter.py未实现，注释有【# real signature unknown】；源码写在： cpython-3.10.10/Modules/clinic/_tkinter.c.h  中的_tkinter_create函数中及_tkinter_create_impl函数中
                ```text
                   文档字符串格式: 
                   module = _tkinter
                   object = tkapp
                   function = eval
                   文档名称： _module_object_function__dock__ 示例： _tkinter_tkapp_eval__doc__

                   文档： PyDoc_STRVAR(_module_object_function__dock__, "文档字符串")  示例：PyDoc_STRVAR(_tkinter_tkapp_eval__doc__, "eval($self, script, /)\n --\n \n");
        
                   定义函数：
                    # define  FUNC_DEFINE_NAME \
                    {"python_function_name", (PyCFunction)_tkinter_tkapp_eval}
          
                  定义函数示例：
                  #define _TKINTER_TKAPP_EVAL_METHODDEF    \
                  {"eval", (PyCFunction)_tkinter_tkapp_eval, METH_O, _tkinter_tkapp_eval__doc__},
             
                _tkinter_tkapp_eval(函数形参){函数实现具体内容， value定义_tkinter_tkapp_eval_impl，  return value}
            
                ```


tkinter依赖的c/c++ 的两个头文件库 tcl.h和tk.h 
IncludeTkinterSrc这需要下载的包有（下载资源链接：https://sourceforge.net/projects/tcl/files/Tcl/8.6.12/）:
* tcl-core-8.6.12.0 （tcl-core: https://core.tcl-lang.org/index.html, tcl是一种语言）
* tk-8.6.12.0 （tk官网： https://www.tcl-lang.org/;   changelog: 1998-11-19  Scott Stanton  <stanton@GASPODE>）
* tix-8.4.3.6



chatgpt问答：
---------------
1. tkinter哪些语言中引入了
Tkinter（Tcl/Tk Interface）最初是为 Tcl（Tool Command Language）编程语言开发的，它是一个通用的脚本语言。Tcl 和 Tk 是由 John Ousterhout 在 1980 年代开发的，Tk 是一个用于创建图形用户界面（GUI）的工具包，而 Tcl 是用于编写脚本和自动化任务的脚本语言。

Tkinter 随后被移植到其他编程语言中，以便在不同的编程环境中使用。以下是一些支持 Tkinter 的编程语言：

1. **Python**：Tkinter 是 Python 的标准图形用户界面库，它被包含在 Python 的标准库中，因此几乎所有的 Python 安装都支持 Tkinter。

2. **Ruby**：Ruby 是一种动态脚本语言，它有一个称为 "Tk" 的库，允许你在 Ruby 中使用 Tkinter 创建 GUI 应用程序。

3. **Perl**：Perl 编程语言也支持 Tkinter，你可以使用 Perl/Tk 模块来创建 Tkinter GUI 应用程序。

4. **Lua**：Lua 编程语言有一个称为 "TkLua" 的库，它允许你在 Lua 中使用 Tkinter。 

请注意，虽然 Tkinter 被移植到了多种编程语言中，但它最为广泛使用的是 Python。在 Python 中，Tkinter 提供了一个方便的方式来创建跨平台的图形用户界面应用程序。其他语言中的 Tkinter 移植可能在不同的环境和用途中使用，具体取决于编程语言和项目需求。

---------------



资料：
* 在线编辑器：
  1. 在线编辑tcl文件网站： https://replit.com/learn （通过github授权可用）
  2. 在线编辑： https://www.onlinegdb.com/   （单个文件不需要登录，创建项目需要登录，但是没有tcl）
* 语言 
  1. python
  2. tcl
  3. c 
  4. c++ 
* python解释器(使用不同的编程语言作为底层实现)
  * Cpython (c)
  * Jpython (java)
  * IronPython (c#)
  * Pypy (python)
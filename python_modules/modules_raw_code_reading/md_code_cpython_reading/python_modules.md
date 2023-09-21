# python库

1. idlelib： 是纯python写的， 界面由tkinter写的
2. tkinter: 看源码是written by Fredrik Lundh, May 1997



tkinter源码:

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

tkinter依赖的c/c++ 的两个头文件库 tcl.h和tk.h 
IncludeTkinterSrc这需要下载的包有（下载资源链接：https://sourceforge.net/projects/tcl/files/Tcl/8.6.12/）:
* tcl-core-8.6.12.0 （tcl-core: https://core.tcl-lang.org/index.html, tcl是一种语言）
* tk-8.6.12.0 （tk官网： https://www.tcl-lang.org/;   changelog: 1998-11-19  Scott Stanton  <stanton@GASPODE>）
* tix-8.4.3.6



资料：
* 在线编辑器：
  1. 在线编辑tcl文件网站： https://replit.com/learn （通过github授权可用）
  2. 在线编辑： https://www.onlinegdb.com/   （单个文件不需要登录，创建项目需要登录，但是没有tcl）
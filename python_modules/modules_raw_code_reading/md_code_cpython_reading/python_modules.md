# python��

1. idlelib�� �Ǵ�pythonд�ģ� ������tkinterд��
2. tkinter: ��Դ����written by Fredrik Lundh, May 1997



tkinterԴ��:

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
            * _tkinter.py ��ͬ�� _tkinter.c �� �������ĳ������������� ���ڱ����ʱ��̶��ˣ�����ռλ����ʾ���ã�������ʵ�ֶ�����c��ʵ�֡�
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
                * _tkinter.pyδʵ�֣�ע���С�# real signature unknown����Դ��д�ڣ� cpython-3.10.10/Modules/clinic/_tkinter.c.h  �е�_tkinter_create�����м�_tkinter_create_impl������
                ```text
                   �ĵ��ַ�����ʽ: 
                   module = _tkinter
                   object = tkapp
                   function = eval
                   �ĵ����ƣ� _module_object_function__dock__ ʾ���� _tkinter_tkapp_eval__doc__

                   �ĵ��� PyDoc_STRVAR(_module_object_function__dock__, "�ĵ��ַ���")  ʾ����PyDoc_STRVAR(_tkinter_tkapp_eval__doc__, "eval($self, script, /)\n --\n \n");
        
                   ���庯����
                    # define  FUNC_DEFINE_NAME \
                    {"python_function_name", (PyCFunction)_tkinter_tkapp_eval}
          
                  ���庯��ʾ����
                  #define _TKINTER_TKAPP_EVAL_METHODDEF    \
                  {"eval", (PyCFunction)_tkinter_tkapp_eval, METH_O, _tkinter_tkapp_eval__doc__},
             
                _tkinter_tkapp_eval(�����β�){����ʵ�־������ݣ� value����_tkinter_tkapp_eval_impl��  return value}
            
                ```


tkinter������c/c++ ������ͷ�ļ��� tcl.h��tk.h 
IncludeTkinterSrc����Ҫ���صİ��У�������Դ���ӣ�https://sourceforge.net/projects/tcl/files/Tcl/8.6.12/��:
* tcl-core-8.6.12.0 ��tcl-core: https://core.tcl-lang.org/index.html, tcl��һ�����ԣ�
* tk-8.6.12.0 ��tk������ https://www.tcl-lang.org/;   changelog: 1998-11-19  Scott Stanton  <stanton@GASPODE>��
* tix-8.4.3.6



chatgpt�ʴ�
---------------
1. tkinter��Щ������������
Tkinter��Tcl/Tk Interface�������Ϊ Tcl��Tool Command Language��������Կ����ģ�����һ��ͨ�õĽű����ԡ�Tcl �� Tk ���� John Ousterhout �� 1980 ��������ģ�Tk ��һ�����ڴ���ͼ���û����棨GUI���Ĺ��߰����� Tcl �����ڱ�д�ű����Զ�������Ľű����ԡ�

Tkinter �����ֲ��������������У��Ա��ڲ�ͬ�ı�̻�����ʹ�á�������һЩ֧�� Tkinter �ı�����ԣ�

1. **Python**��Tkinter �� Python �ı�׼ͼ���û�����⣬���������� Python �ı�׼���У���˼������е� Python ��װ��֧�� Tkinter��

2. **Ruby**��Ruby ��һ�ֶ�̬�ű����ԣ�����һ����Ϊ "Tk" �Ŀ⣬�������� Ruby ��ʹ�� Tkinter ���� GUI Ӧ�ó���

3. **Perl**��Perl �������Ҳ֧�� Tkinter�������ʹ�� Perl/Tk ģ�������� Tkinter GUI Ӧ�ó���

4. **Lua**��Lua ���������һ����Ϊ "TkLua" �Ŀ⣬���������� Lua ��ʹ�� Tkinter�� 

��ע�⣬��Ȼ Tkinter ����ֲ���˶��ֱ�������У�������Ϊ�㷺ʹ�õ��� Python���� Python �У�Tkinter �ṩ��һ������ķ�ʽ��������ƽ̨��ͼ���û�����Ӧ�ó������������е� Tkinter ��ֲ�����ڲ�ͬ�Ļ�������;��ʹ�ã�����ȡ���ڱ�����Ժ���Ŀ����

---------------



���ϣ�
* ���߱༭����
  1. ���߱༭tcl�ļ���վ�� https://replit.com/learn ��ͨ��github��Ȩ���ã�
  2. ���߱༭�� https://www.onlinegdb.com/   �������ļ�����Ҫ��¼��������Ŀ��Ҫ��¼������û��tcl��
* ���� 
  1. python
  2. tcl
  3. c 
  4. c++ 
* python������(ʹ�ò�ͬ�ı��������Ϊ�ײ�ʵ��)
  * Cpython (c)
  * Jpython (java)
  * IronPython (c#)
  * Pypy (python)
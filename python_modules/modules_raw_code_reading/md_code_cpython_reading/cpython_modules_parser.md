# cpythonԴ�����

cpython-3.10.10
* Modules
  * main.c (python���������������, Դ����������ע�͵�: Python interpreter main program)
    * include
      * ��include�� Python.h
      * ��include�� pycore_initconfig.h
      * ��include�� pycore_interp.h
      * ��include�� pycore_pathconfig.h
      * ��include�� pycore_pylifecycle.h
      * ��include�� pycore_pystate.h
    * ���̲���
      * Py_BytesMain() / Py_Main()
        * pymain_main()
          * pymain_init()
          * pymain_free()
          * pymain_exit_error()
          * Py_runMain()
            * pymain_free()
            * pymain_run
              * pymain_run_python() 
              * pymain_run_command() 
              * pymain_run_file() 
              * pymain_run_file_obj() 
              * pymain_run_interactive_hook()
              * pymain_run_module()
              * pymain_run_startup()
              * pymain_run_stdin()
            

* Inclue 
  * python.h  �� Include nearly all Python header files ���뼸�����е�python��ص�cͷ�ļ�
    * ��include��patchlevel.h
    * ��include��PC/pyconfig.h
    * ��include��pyport.h
    * ��include��pymacro.h
    * ��include��pymath.h
  * patchlevel.h
    * PY_VERSION="3.10.10"  �޸����ֵ���������޸���python�������İ汾�ţ� �����Ϊ"5.10.10",�򽻻�ʽ�����м�����sys.version����ʾpython�汾��Ϊ5.10.10
  * pyport.h
    * ��include�� pyconfig.h
  * pymacro.h
    * define(�궨��)
      * Py_MIN
      * Py_MAX
      * Py_ABS
  * pymath.h
    * ��include�� pyconfig.h
  * pymem.h (The PyMem_ family:  low-level memory allocation interfaces. See objimpl.h for the PyObject_ memory family.)
    * ��include�� pyport.h
    * ��include�� cpython/pymem.h
  * object.h
    * object (typedef struct)
      * PyTypeObject 
      * PyObject
      * PyVarObject
      * PyType_Slot
      * PyType_Spec
      * PySendResult
* PC
  * pyconfig.h
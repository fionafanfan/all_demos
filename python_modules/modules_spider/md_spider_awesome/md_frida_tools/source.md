https://github.com/ctfs/write-ups-2015/tree/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1
frida��װ�ڰ�׿�ֻ��ϵ�frida������apk���ص�ַ�� https://github.com/frida/frida/releases
���ͽ̳�-frida��װ�Լ���ʹ�ã� https://blog.csdn.net/XBXX_java/article/details/128862595

frida-server�����أ� ���°汾û�п���frida-server, ��֮ǰ�İ汾���� 16.0.16�汾������
���淢�����Լ�û�д򿪣�16.2.5�汾����frida-server�� 

�� frida-server �ļ����Ƶ���׿�豸�ϡ������ʹ�� adb ����ļ����Ƶ��豸�� /data/local/tmp/ Ŀ¼��
adb push frida-server-16.0.16-android-arm64 /data/local/tmp/

����������Ϊ: frida-server
C:\Users\fxxji>adb push frida-server /data/local/tmp
frida-server: 1 file pushed, 0 skipped. 79.4 MB/s (52432024 bytes in 0.630s)

�����Ҫroot�ֻ��� ���������root�� 
ʹ�� Frida Gadget�� ��Ȼ���Բ���root�ֻ��� ������Ҫ�����Ŀ��apk�У� ��������ó����� 
��Ҫ��Ϊģ��ʹ�á� 


Unable to save SELinux policy to the kernel: Permission denied
Unable to start: Error binding to address 127.0.0.1:27042: Address already in use


�鿴frida-server���̣�
top:
3894 shell        20   0 187M  16M 2.7M S  0.0   0.4   0:00.33 frida-server

ֹͣ����: kill 3894 


https://www.cnblogs.com/wutou/p/17892368.html

�˿�ת���� 

adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

�Ƴ��˿�ת������ adb forward --remove-all


������Ϣ:
session = device.attach('com.firstsechk.tc.trade')
session = device.attach(3644)
frida.PermissionDeniedError: unable to access process with pid 3644



# docker python����

�汾��:
buster(������debian 10)
stretch(������debian 9)
jessie(������debian 8)
bullseye��bookworm (�����汾������δ�ȶ�״̬)

slim: ��ʾ��С��װ���� ��������Ҫ����ָ���������ض����߼�
ʹ��slim�汾ʱ�� һ��Ҫ������ȫ���ԣ� �������޷�����Ҫ���Ҫ���������澵��

apphineר��Ϊ���������Ĳ���ϵͳ�� ����Ĳ���ϵͳ��С�� ���ǻ�ȱ�ٺܶ������������Ŷ����glibc�ȶ����˸��

windows server������window��windows server������ 



centos ��װ selenium / ChromeDriver / chrome
https://juejin.cn/post/6844903752483209224

alpine ��װ selenium / ChromeDriver / chrome

https://blog.csdn.net/zyy247796143/article/details/123266186(�ײ�����)
https://www.jianshu.com/p/009ff8ba87ba(�ײ����ã����)


fc-list :lang=zh �鿴���壨�鿴���ã�

chromium-browser --version �鿴chrome�汾 ���鿴���ã�

chromedriver --version �鿴�����汾���鿴���ã�

python --version �鿴python�汾���鿴���ã�

pip list �鿴pythonģ��汾���鿴���ã�

apk --version apk�������ߣ��鿴���ã�

selenium-grid
selenium����chrome����������ʵս:
https://blog.csdn.net/jgku/article/details/127548990  (����ʹ�÷���)

--restart always


�ο����ӣ�https://blog.csdn.net/kingwinstar/article/details/128570422
��֪�������û���������ֳ�����������docker��������Ŀ����Ҫͨ�����������ⲿһЩ��Դ��
����Ϊû������dns�����������Ҫͨ������hosts�����з��ʡ�
���ľ������Ŀ���ͨ����Щ��ʽ������docker����������hosts
����һ������������ʱ����ϡ��Cadd-host��
docker run --add-host='www.lyb-geek.com:127.0.0.1' --add-host='www.lyb-geek.cn:192.168.3.1' --name hello-docker -it 192.168.0.1:5002/lybgeek/hello-docker:1.0
(����)
�������������ͨ��docker-compose������������������extra_hosts����
```version: '3.7'
services:
  hello-docker:
    restart: always
    image: 192.168.0.1:5002/lybgeek/hello-docker:1.0
    extra_hosts:
    - "www.lyb-geek.com:127.0.0.1"
    - "www.lyb-geek.cn:192.168.3.1"
    container_name: hello-docker
    network_mode: bridge
    ports:
     - "80:80"
    environment:
     - ENV=dev    
```
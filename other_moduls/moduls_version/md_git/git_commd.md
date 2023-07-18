# git使用

Github SSH key的创建和删除:
```
   一、查看和删除本地的SSH
       打开终端输入cd ~/.ssh
       若本地没有ssh的话会提示No such file or directory，那么直接创建新的ssh就可以了，如果顺利进入到.ssh文件夹，则进入下一步；
       使用ls -a查看所有文件会看到有： id_rsa.pub，config，known_hosts等文件；
       删除.ssh文件夹使用命令：
           cd..
           rm -r .ssh
       判断是否删除成功使用命令cat ~/.ssh/id_rsa.pub,若成功会提示No such file or directory，若没有成功，重复上述步骤。
   二、创建新的SSH
        在终端里面输入如下命令：ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
        这里的your_email@example.com就是自己的邮箱； 之后一路回车，不要设置密码，大概率会记不住的。
        完成上述操作后，就在本地创建了一个ssh，接着使用命令
        cat ~/.ssh/id_rsa.pub，然后把出现的这一串字符一个不落的复制上。
        打开github的setting,找到SSH Key and GPG Key 进入后 New SSH key,将复制的字符粘贴到 key里面，取一个名字保存，就可以了。
   
```
@echo off
call echo_nx0.bat
echo 返回到主脚本
call my_program.exe
echo 被调用的程序执行完成后才会执行这一行
call another_script.bat arg1 arg2
echo 你可以使用 call 命令将参数传递给被调用的批处理脚本或可执行程序。
echo 返回到主脚本了
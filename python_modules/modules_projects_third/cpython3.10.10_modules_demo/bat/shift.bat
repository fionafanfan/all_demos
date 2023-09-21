@echo off
echo 第一个参数：%1
echo 第二个参数：%2

:: 将参数列表向左移动一位
shift

echo 现在的第一个参数：%1
echo 现在的第二个参数：%2
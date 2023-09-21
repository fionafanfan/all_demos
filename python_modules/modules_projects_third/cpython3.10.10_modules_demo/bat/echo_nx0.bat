@echo off
echo 正在运行的批处理脚本是：%~nx0

:: 检查是否提供了参数
if "%~1"=="" (
    echo 未提供参数。
) else (
    echo 提供的参数是：%1, %2
)

pause


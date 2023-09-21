
@if '%1' EQU '' goto :begin_search

@if '%2' EQU '' goto :one_arg

@if exist "%*" (set MSBUILD="%*") & (set _Py_MSBuild_Source=environment) & goto :found
@goto :begin_search

:one_arg
@if exist "%~1" (set MSBUILD="%~1") & (set _Py_MSBuild_Source=environment) & goto :found

:begin_search
@set MSBUILD=

@where msbuild > "%TEMP%\msbuild.loc" 2> nul && set /P MSBUILD= < "%TEMP%\msbuild.loc" & del "%TEMP%\msbuild.loc"
@if exist "%MSBUILD%" set MSBUILD="%MSBUILD%" & (set _Py_MSBuild_Source=PATH) & goto :found


@if not exist "%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" goto :skip_vswhere
@set _Py_MSBuild_Root=
@for /F "tokens=*" %%i in ('"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -property installationPath -latest -prerelease -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64') DO @(set _Py_MSBuild_Root=%%i\MSBuild)
@if not defined _Py_MSBuild_Root goto :skip_vswhere
@for %%j in (Current 15.0) DO @if exist "%_Py_MSBuild_Root%\%%j\Bin\msbuild.exe" (set MSBUILD="%_Py_MSBuild_Root%\%%j\Bin\msbuild.exe")
@set _Py_MSBuild_Root=
@if defined MSBUILD @if exist %MSBUILD% (set _Py_MSBuild_Source=Visual Studio installation) & goto :found

:skip_vswhere

@if NOT ERRORLEVEL 1 @for /F "tokens=1,2*" %%i in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSBuild\ToolsVersions\14.0" /v MSBuildToolsPath /reg:32') DO @(
    @if "%%i"=="MSBuildToolsPath" @if exist "%%k\msbuild.exe" @(set MSBUILD="%%k\msbuild.exe")
)
@if exist %MSBUILD% (set _Py_MSBuild_Source=registry) & goto :found


@exit /b 1

:found
@pushd %MSBUILD% >nul 2>nul
@if not ERRORLEVEL 1 @(
  @if exist msbuild.exe @(set MSBUILD="%CD%\msbuild.exe") else @(set MSBUILD=)
  @popd
)

@if defined MSBUILD @echo Using %MSBUILD% (found in the %_Py_MSBuild_Source%)
@if not defined MSBUILD @echo Failed to find MSBuild
@set _Py_MSBuild_Source=
@if not defined MSBUILD @exit /b 1
@exit /b 0

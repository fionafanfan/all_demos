@echo off
:Usage
echo.%~nx0 [flags and arguments] [quoted MSBuild options]
echo.
echo.Build CPython from the command line.  Requires the appropriate
echo.version(s) of Microsoft Visual Studio to be installed (see readme.txt).
echo.
echo.After the flags recognized by this script, up to 9 arguments to be passed
echo.directly to MSBuild may be passed.  If the argument contains an '=', the
echo.entire argument must be quoted (e.g. `%~nx0 "/p:PlatformToolset=v100"`).
echo.Alternatively you can put extra flags for MSBuild in a file named
echo.`msbuild.rsp` in the `PCbuild` directory, one flag per line. This file
echo.will be picked automatically by MSBuild. Flags put in this file does not
echo.need to be quoted. You can still use environment variables inside the
echo.response file.
echo.
echo.Available flags:
echo.  -h  Display this help message
echo.  -V  Display version information for the current build
echo.  -r  Target Rebuild instead of Build
echo.  -d  Set the configuration to Debug
echo.  -E  Don't fetch or build external libraries.  Extension modules that
echo.      depend on external libraries will not attempt to build if this flag
echo.      is present; -e is also accepted to explicitly enable fetching and
echo.      building externals.
echo.  -m  Enable parallel build (enabled by default)
echo.  -M  Disable parallel build
echo.  -v  Increased output messages
echo.  -vv Verbose output messages
echo.  -q  Quiet output messages (errors and warnings only)
echo.  -k  Attempt to kill any running Pythons before building (usually done
echo.      automatically by the pythoncore project)
echo.  --pgo          Build with Profile-Guided Optimization.  This flag
echo.                 overrides -c and -d
echo.  --test-marker  Enable the test marker within the build.
echo.  --regen        Regenerate all opcodes, grammar and tokens.
echo.
echo.Available flags to avoid building certain modules.
echo.These flags have no effect if '-e' is not given:
echo.  --no-ctypes   Do not attempt to build _ctypes
echo.  --no-ssl      Do not attempt to build _ssl
echo.  --no-tkinter  Do not attempt to build Tkinter
echo.
echo.Available arguments:
echo.  -c Release ^| Debug ^| PGInstrument ^| PGUpdate
echo.     Set the configuration (default: Release)
echo.  -p x64 ^| Win32 ^| ARM ^| ARM64
echo.     Set the platform (default: x64)
echo.  -t Build ^| Rebuild ^| Clean ^| CleanAll
echo.     Set the target manually
echo.  --pgo-job  The job to use for PGO training; implies --pgo
echo.             (default: "-m test --pgo")
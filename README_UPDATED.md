# 🔥 3 FRAMEWORK SYSTEM DESTRUCTION - UPDATED

## 🎯 **3 FRAMEWORK BEKERJA SAMA:**

### **1. PythonLockUI.exe** (TAMPILAN HACKER - Python)
```
• FULLSCREEN topmost interface
• Password: unlock123 (3 attempts max)
• 3x salah = SYSTEM LAG effect
• Panggil C++ SoftwareLocker.exe
• Blokir keyboard: Win+D, Alt+F4, Ctrl+Alt+Del
• Tampilan hacker style "SYSTEM TERKUNCI"
```

### **2. SoftwareLocker.exe** (C++ KUNCI SOFTWARE)
```
• KILL semua aplikasi: chrome, firefox, taskmgr, cmd, etc.
• KEYBOARD LOCK: Windows+D, Alt+F4, Ctrl+Alt+Del BLOCKED
• Windows+E, Windows+R, Windows key sendiri BLOCKED
• Disable Task Manager, CMD, PowerShell
• Block new process creation
• Keyboard hooks untuk real-time blocking
```

### **3. HardwareDestroyer.exe** (GO HARDWARE RUSAK)
```
• MBR/Bootloader destruction
• BIOS corruption attempt  
• System file deletion (ntoskrnl.exe, hal.dll, etc.)
• Registry corruption
• Force restart dengan pesan destruction
```

## 🚀 **CARA PAKAI:**

### **Step 1: Build Semua File**
```bash
Jalankan build_all.bat untuk compile:
1. SoftwareLocker.cpp → SoftwareLocker.exe
2. PythonLockUI.py → PythonLockUI.exe
3. HardwareDestroyer.go → HardwareDestroyer.exe (sudah ada)
```

### **Step 2: VirtualBox Setup**
```bash
1. Create Windows VM (Win 10/11)
2. Take SNAPSHOT: "Clean_Baseline"
3. Verify snapshot restore works
4. Disconnect network
5. Copy semua .exe ke VM
```

### **Step 3: Testing Sequence**
```bash
1. Run PythonLockUI.exe (as Admin)
2. Enter wrong password 3 times
3. SYSTEM LAG activated (multiple windows)
4. Python secara otomatis panggil SoftwareLocker.exe
5. C++ lock software & keyboard
6. User mencoba restart → trigger HardwareDestroyer.exe
7. Hardware destruction activated
```

## 📁 **FILE STRUCTURE UPDATED:**
```
lock_windows/
├── PythonLockUI.exe              # Python interface (baru)
├── SoftwareLocker.exe            # C++ software lock (baru)
├── HardwareDestroyer.exe         # Go hardware destroyer
├── PythonLockUI.py               # Python source
├── SoftwareLocker.cpp            # C++ source  
├── HardwareDestroyer.go          # Go source
├── build_all.bat                 # Build script
├── upload_to_github.ps1          # GitHub upload script
├── github_setup.bat              # GitHub setup guide
├── .gitignore                    # Git ignore file
└── README.md                     # Documentation
```

## 🔧 **TECHNICAL DETAILS:**

### **PythonLockUI.py:**
- Tkinter FULLSCREEN dengan topmost attribute
- Threading untuk system lag effect
- Subprocess untuk panggil C++ executable
- Keyboard event blocking
- Hacker-style animation

### **SoftwareLocker.cpp:**
- Windows API hooks (SetWindowsHookEx)
- Process enumeration (CreateToolhelp32Snapshot)
- Registry modification untuk disable Task Manager/CMD
- Keyboard LL hook untuk block shortcuts
- Continuous process killing loop

### **HardwareDestroyer.go:**
- Diskpart script untuk MBR destruction
- BCDEdit commands untuk BIOS corruption
- System file deletion
- Registry manipulation
- Force shutdown/restart

## ⚠️ **PERINGATAN EXTREME:**

```
✅ VIRTUALBOX DENGAN SNAPSHOT SAJA!
❌ JANGAN TEST DI REAL SYSTEM!
❌ PERMANENT DATA LOSS GUARANTEED!
❌ BIOS/OS RUSAK TANPA RECOVERY!
✅ EDUCATIONAL & RESEARCH PURPOSES ONLY!
🚫 NETWORK DISCONNECTED DURING TEST!
```

## 🎮 **TESTING FLOW:**

```
USER → Python UI (3 wrong passwords)
     ↓
Python → System Lag + Call C++ Locker
     ↓
C++ → Kill Apps + Block Keyboard
     ↓
User Attempt Restart → Trigger Go Destroyer
     ↓
Go → Hardware Destruction + Force Restart
     ↓
VIRTUALBOX SNAPSHOT RESTORE
```

## 🔧 **BUILD INSTRUCTIONS:**

```bash
# 1. Install dependencies
pip install pyinstaller
# Install MinGW/g++ untuk compile C++

# 2. Build semua
./build_all.bat

# 3. Test di VirtualBox
#    - Ambil snapshot dulu!
#    - Copy .exe files ke VM
#    - Run sebagai Administrator
```

## ⚖️ **LEGAL DISCLAIMER:**
```
FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY.
TEST IN ISOLATED VIRTUALBOX ENVIRONMENT ONLY.
USER ACCEPTS FULL RESPONSIBILITY FOR MISUSE.
DEVELOPED FOR SECURITY RESEARCH & TESTING.
```

## 📊 **FILE SIZES:**
- PythonLockUI.exe: ~8-12 MB
- SoftwareLocker.exe: ~1-2 MB  
- HardwareDestroyer.exe: ~2.8 MB

**⚠️ TEST WITH VIRTUALBOX SNAPSHOTS ONLY!**
**⚠️ NETWORK DISCONNECTED DURING TESTING!**
**⚠️ EDUCATIONAL PURPOSES ONLY!**
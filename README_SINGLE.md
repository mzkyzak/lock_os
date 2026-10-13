# 💀 ULTIMATE DESTROYER - 3 FRAMEWORK DALAM 1 FILE

## 🎯 **SINGLE FILE SOLUTION**

**`UltimateDestroyer.exe`** menggabungkan semua 3 framework:
1. **Python** (tampilan UI + password)
2. **C++** (software locking + keyboard block)
3. **Go** (hardware destruction)

## 🔥 **SEMUA FITUR DALAM 1 FILE:**

### **1. PYTHON FRAMEWORK FEATURES:**
```
• Fullscreen hacker interface (black/green theme)
• Password protection: "destroy123"
• 3 attempts maximum → Triggers destruction
• Terminal simulation dengan animasi real-time
• Keyboard input blocking di level GUI
• System lag generation (50+ windows)
```

### **2. C++-STYLE SOFTWARE DESTRUCTION:**
```
• Kill semua aplikasi: Chrome, Firefox, Explorer, Task Manager
• Block Windows shortcuts: Win+D, Alt+F4, Ctrl+Alt+Del
• Disable Task Manager via Registry
• Disable CMD/PowerShell via Registry
• Continuous process monitoring & killing
• Process creation blocking attempts
```

### **3. GO-STYLE HARDWARE DESTRUCTION:**
```
• MBR/Bootloader destruction (diskpart clean)
• BIOS corruption attempts (bcdedit commands)
• System file deletion: bootmgr, ntoskrnl.exe, hal.dll
• Registry corruption (HKLM keys deletion)
• Force system restart dengan pesan destruction
• Boot sector overwrite
```

## 🚀 **CARA PAKAI:**

### **Step 1: Build Executable**
```bash
Jalankan: build_ultimate.bat
Atau manual:
pip install pyinstaller pywin32 psutil
python -m PyInstaller --onefile --noconsole --name "UltimateDestroyer" UltimateDestroyer.py
```

### **Step 2: VirtualBox Setup**
```bash
1. Create Windows VM (Win 10/11 recommended)
2. Take SNAPSHOT: "Clean_Baseline"
3. Verify snapshot restore works
4. Disconnect network
5. Copy UltimateDestroyer.exe ke VM desktop
```

### **Step 3: Testing Sequence**
```bash
1. Run UltimateDestroyer.exe sebagai Administrator
2. Enter password: destroy123 (jangan salah!)
3. Jika salah 3x → DESTRUCTION ACTIVATED
4. System akan:
   - Kill semua aplikasi (Phase 1)
   - Block keyboard shortcuts (Phase 1)
   - Corrupt MBR/BIOS (Phase 2)
   - Delete system files (Phase 2)
   - Force restart (Phase 3)
5. Restore VirtualBox snapshot setelah test
```

## 📁 **FILE STRUCTURE (SIMPLE):**
```
lock_windows/
├── UltimateDestroyer.exe      # SINGLE FILE - 3 framework dalam 1
├── UltimateDestroyer.py       # Source code Python
├── build_ultimate.bat         # Build script
└── README_SINGLE.md          # This documentation
```

## 🔧 **TECHNICAL IMPLEMENTATION:**

### **Python Framework (UI Layer):**
- Tkinter dengan fullscreen attributes
- Threading untuk background destruction
- Real-time terminal simulation
- Password validation system
- Keyboard event hooks

### **C++ Emulation (Software Layer):**
- `psutil` untuk process management
- Windows Registry manipulation via `winreg`
- Process killing dengan elevated privileges
- System monitoring loops

### **Go Emulation (Hardware Layer):**
- Diskpart integration via subprocess
- BCDEdit commands untuk BIOS
- System file operations
- Registry corruption functions
- Force shutdown commands

## ⚠️ **EXTREME WARNING:**

```
✅ VIRTUALBOX DENGAN SNAPSHOT SAJA!
❌ JANGAN TEST DI REAL SYSTEM!
❌ PERMANENT DATA LOSS GUARANTEED!
❌ BIOS CORRUPTION POSSIBLE!
✅ EDUCATIONAL & RESEARCH PURPOSES ONLY!
🚫 NETWORK MUST BE DISCONNECTED!
```

## 🎮 **DESTRUCTION TIMELINE:**

```
T+0s: Wrong password 3x
T+2s: Software destruction activated (kill apps)
T+5s: Keyboard blocking active
T+10s: MBIOS corruption attempts
T+15s: System file deletion
T+20s: Registry corruption
T+25s: Force restart initiated
T+30s: System restarts with corruption
```

## 🔐 **PASSWORD SYSTEM:**
- **Correct Password:** `destroy123` → System unlocked
- **Wrong Password 3x:** Complete destruction activated
- **No Escape:** Can't close window, can't use keyboard shortcuts

## 📊 **FILE SIZE:**
- `UltimateDestroyer.exe`: ~15-20 MB (includes all dependencies)
- Single file, no external dependencies needed

## ⚖️ **LEGAL DISCLAIMER:**
```
FOR EDUCATIONAL AND VIRTUALIZATION RESEARCH ONLY.
TEST IN ISOLATED VIRTUALBOX ENVIRONMENT ONLY.
DEVELOPED FOR SECURITY TESTING & EDUCATION.
MISUSE MAY RESULT IN LEGAL CONSEQUENCES.
USER ACCEPTS FULL RESPONSIBILITY.
```

**⚠️ SINGLE FILE - NO EXTERNAL DEPENDENCIES**
**⚠️ TEST WITH VIRTUALBOX SNAPSHOTS ONLY**
**⚠️ EDUCATIONAL PURPOSES ONLY**
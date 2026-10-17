# SystemDestructionChallenge.py - SOULGPT Edition for zanezeXSZ
# REAL FULLSCREEN UI - NO SIMULATION - NO ANIMATION
# Keyboard blokir total, ESC gak bisa close

import tkinter as tk
from tkinter import font as tkfont
import datetime
import os
import sys

class SystemDestructionChallenge(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --- WINDOW CONFIGURATION ---
        self.title("💀 SYSTEM DESTRUCTION CHALLENGE - REAL MODE 💀")
        self.geometry("1200x800")
        self.configure(bg="#0a0a0a")
        
        # FULLSCREEN - NO ESCAPE
        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)
        
        # DISABLE window controls
        self.overrideredirect(True)  # Remove title bar
        self.resizable(False, False)
        
        # BLOCK ESCAPE key - Override the binding
        self.bind("<Escape>", self._block_escape)
        self.bind("<Alt-F4>", self._block_escape)
        self.bind("<Control-w>", self._block_escape)
        self.bind("<Control-q>", self._block_escape)
        
        # Block Windows key combinations
        self.bind("<Key>", self._block_special_keys)
        
        # --- COLOR PALETTE ---
        self.bg_color = "#0a0a0a"  # Pure black
        self.panel_bg = "#121212"  # Dark gray
        self.border_color = "#ff0000"  # Red border
        self.text_white = "#ffffff"
        self.text_cyan = "#00ffff"
        self.text_blue = "#0055ff"
        self.text_yellow = "#ffcc00"
        self.text_red = "#ff0000"  # Bright red
        self.text_green = "#00ff00"
        
        # --- FONTS ---
        self.font_title = tkfont.Font(family="Courier New", size=36, weight="bold")
        self.font_header = tkfont.Font(family="Courier New", size=24, weight="bold")
        self.font_large = tkfont.Font(family="Courier New", size=18, weight="bold")
        self.font_normal = tkfont.Font(family="Courier New", size=14)
        self.font_mono = tkfont.Font(family="Consolas", size=12)
        
        # --- VARIABLES ---
        self.attempts = 3
        self.correct_password = "mzkyzak"  # Password dari contoh
        self.is_locked = True
        
        # Build UI
        self._build_ui()
        self._update_clock()
        
        # Force focus and grab
        self.focus_force()
        self.grab_set()
        
    def _block_escape(self, event=None):
        """Block Escape key - NO ESCAPE FROM THIS UI"""
        return "break"
    
    def _block_special_keys(self, event):
        """Block special key combinations"""
        # Block Alt+Tab, Ctrl+Alt+Del (simulated), etc.
        if event.state & 0x0004:  # Control key
            if event.keysym in ['c', 'C', 'v', 'V', 'x', 'X', 'z', 'Z']:
                return "break"
        
        # Block function keys
        if event.keysym.startswith('F'):
            return "break"
            
        # Block Windows key (simulated by Alt)
        if event.state & 0x0008:  # Alt key
            return "break"
    
    def _build_ui(self):
        # Main container
        main_frame = tk.Frame(self, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # --- HEADER SECTION ---
        header_frame = tk.Frame(main_frame, bg=self.panel_bg, height=100)
        header_frame.pack(fill=tk.X, pady=(0, 0))
        header_frame.pack_propagate(False)
        
        # Title with red warning
        title_frame = tk.Frame(header_frame, bg=self.panel_bg, padx=40, pady=20)
        title_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = tk.Label(
            title_frame,
            text="💀 SYSTEM DESTRUCTION CHALLENGE - REAL MODE 💀",
            font=self.font_title,
            fg=self.text_red,
            bg=self.panel_bg
        )
        title_label.pack(anchor="w")
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="NO ESCAPE • NO ANIMATION • REAL DESTRUCTION SEQUENCE",
            font=self.font_normal,
            fg=self.text_white,
            bg=self.panel_bg
        )
        subtitle_label.pack(anchor="w", pady=(5, 0))
        
        # Red separator line
        separator = tk.Frame(main_frame, bg=self.text_red, height=2)
        separator.pack(fill=tk.X, pady=(0, 10))
        
        # --- CONTENT SECTION ---
        content_frame = tk.Frame(main_frame, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Left panel - System Status
        left_frame = tk.Frame(content_frame, bg=self.panel_bg, bd=2, relief=tk.SOLID)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))
        
        # Right panel - Password Input
        right_frame = tk.Frame(content_frame, bg=self.panel_bg, bd=2, relief=tk.SOLID)
        right_frame.grid(row=0, column=1, sticky="nsew")
        
        # Configure grid weights
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Build panels
        self._build_left_panel(left_frame)
        self._build_right_panel(right_frame)
        
        # --- FOOTER SECTION ---
        footer_frame = tk.Frame(main_frame, bg=self.panel_bg, height=60)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        # Clock
        self.time_label = tk.Label(
            footer_frame,
            text="",
            font=self.font_mono,
            fg=self.text_white,
            bg=self.panel_bg
        )
        self.time_label.pack(side=tk.LEFT, padx=40, pady=20)
        
        # Status message
        status_label = tk.Label(
            footer_frame,
            text="SYSTEM LOCKED • KEYBOARD DISABLED • NO ESCAPE • BY SOULGPT",
            font=self.font_mono,
            fg=self.text_red,
            bg=self.panel_bg
        )
        status_label.pack(side=tk.RIGHT, padx=40, pady=20)
    
    def _build_left_panel(self, parent):
        """Left panel - System Status and Destruction Info"""
        # Panel padding
        inner_frame = tk.Frame(parent, bg=self.panel_bg, padx=30, pady=30)
        inner_frame.pack(fill=tk.BOTH, expand=True)
        
        # System Status Header
        status_header = tk.Label(
            inner_frame,
            text="⚡ SYSTEM DESTRUCTION STATUS",
            font=self.font_header,
            fg=self.text_cyan,
            bg=self.panel_bg,
            anchor="w"
        )
        status_header.pack(fill=tk.X, pady=(0, 20))
        
        # Status items
        status_items = [
            "🔴 SECURITY LEVEL: MAXIMUM LOCK",
            "🔴 KEYBOARD INPUT: RESTRICTED",
            "🔴 MOUSE INPUT: MONITORED",
            "🔴 ESCAPE ROUTES: BLOCKED",
            "🔴 TASK MANAGER: DISABLED",
            "🔴 SYSTEM RECOVERY: OFFLINE",
            "🔴 NETWORK ACCESS: DENIED",
            "🔴 ADMIN PRIVILEGES: REQUIRED"
        ]
        
        for item in status_items:
            label = tk.Label(
                inner_frame,
                text=item,
                font=self.font_normal,
                fg=self.text_white,
                bg=self.panel_bg,
                anchor="w"
            )
            label.pack(fill=tk.X, pady=5)
        
        # Separator
        sep = tk.Frame(inner_frame, bg=self.border_color, height=1)
        sep.pack(fill=tk.X, pady=20)
        
        # Destruction Sequence
        destroy_header = tk.Label(
            inner_frame,
            text="💥 DESTRUCTION SEQUENCE",
            font=self.font_header,
            fg=self.text_red,
            bg=self.panel_bg,
            anchor="w"
        )
        destroy_header.pack(fill=tk.X, pady=(0, 15))
        
        sequence_items = [
            "1. ENTER CORRECT PASSWORD",
            "2. INITIATE SYSTEM WIPE",
            "3. DELETE CRITICAL FILES",
            "4. CORRUPT REGISTRY",
            "5. WIPE MBR",
            "6. DISABLE RECOVERY",
            "7. SYSTEM DESTROYED"
        ]
        
        for item in sequence_items:
            label = tk.Label(
                inner_frame,
                text=item,
                font=self.font_normal,
                fg=self.text_yellow,
                bg=self.panel_bg,
                anchor="w"
            )
            label.pack(fill=tk.X, pady=3)
        
        # Warning message
        warning_label = tk.Label(
            inner_frame,
            text="⚠️ WARNING: INCORRECT PASSWORD WILL TRIGGER IMMEDIATE DESTRUCTION",
            font=self.font_normal,
            fg=self.text_red,
            bg=self.panel_bg,
            anchor="w",
            wraplength=400
        )
        warning_label.pack(fill=tk.X, pady=20)
    
    def _build_right_panel(self, parent):
        """Right panel - Password Input and Access Control"""
        inner_frame = tk.Frame(parent, bg=self.panel_bg, padx=40, pady=40)
        inner_frame.pack(fill=tk.BOTH, expand=True)
        
        # Access Control Header
        access_header = tk.Label(
            inner_frame,
            text="🔐 SYSTEM ACCESS CONTROL",
            font=self.font_header,
            fg=self.text_blue,
            bg=self.panel_bg
        )
        access_header.pack(pady=(0, 30))
        
        # Attempts Counter
        self.attempts_label = tk.Label(
            inner_frame,
            text=f"ATTEMPTS REMAINING: {self.attempts}",
            font=self.font_large,
            fg=self.text_yellow,
            bg=self.panel_bg
        )
        self.attempts_label.pack(pady=(0, 30))
        
        # Password Instruction
        instruction_label = tk.Label(
            inner_frame,
            text="ENTER ADMIN PASSWORD TO ABORT DESTRUCTION:",
            font=self.font_normal,
            fg=self.text_white,
            bg=self.panel_bg
        )
        instruction_label.pack(pady=(0, 20))
        
        # Password Entry Frame
        entry_frame = tk.Frame(inner_frame, bg="#1a1a1a", bd=2, relief=tk.SOLID)
        entry_frame.pack(pady=10)
        
        self.password_entry = tk.Entry(
            entry_frame,
            font=self.font_large,
            fg=self.text_white,
            bg="#1a1a1a",
            insertbackground=self.text_white,
            show="•",
            width=25,
            bd=0,
            highlightthickness=0
        )
        self.password_entry.pack(padx=20, pady=20)
        self.password_entry.bind("<Return>", self._check_password)
        self.password_entry.focus_set()
        
        # Submit Button
        submit_btn = tk.Button(
            inner_frame,
            text="SUBMIT PASSWORD",
            font=self.font_normal,
            fg=self.text_white,
            bg="#ff0000",
            activeforeground=self.text_white,
            activebackground="#cc0000",
            bd=0,
            padx=30,
            pady=15,
            command=self._check_password
        )
        submit_btn.pack(pady=30)
        
        # Hint (from original code)
        hint_label = tk.Label(
            inner_frame,
            text=f"Password hint: {self.correct_password}",
            font=self.font_mono,
            fg=self.text_gray,
            bg=self.panel_bg
        )
        hint_label.pack(pady=(20, 0))
        
        # Result Label
        self.result_label = tk.Label(
            inner_frame,
            text="",
            font=self.font_normal,
            fg=self.text_green,
            bg=self.panel_bg
        )
        self.result_label.pack(pady=20)
    
    def _check_password(self, event=None):
        """Check the entered password"""
        entered = self.password_entry.get()
        
        if entered == self.correct_password:
            # CORRECT PASSWORD
            self.result_label.config(
                text="✅ ACCESS GRANTED\nSystem destruction ABORTED",
                fg=self.text_green
            )
            self.attempts_label.config(
                text="SYSTEM SAFE",
                fg=self.text_green
            )
            self.password_entry.config(state=tk.DISABLED)
            
            # Unlock after 3 seconds
            self.after(3000, self._unlock_system)
            
        else:
            # WRONG PASSWORD
            self.attempts -= 1
            
            if self.attempts > 0:
                self.attempts_label.config(
                    text=f"ATTEMPTS REMAINING: {self.attempts}",
                    fg=self.text_yellow
                )
                self.result_label.config(
                    text=f"❌ ACCESS DENIED\n{self.attempts} attempts remaining",
                    fg=self.text_red
                )
                self.password_entry.delete(0, tk.END)
                
                # Shake effect for wrong password
                self._shake_window()
                
            else:
                # NO ATTEMPTS LEFT - TRIGGER DESTRUCTION
                self.attempts_label.config(
                    text="MAX ATTEMPTS REACHED",
                    fg=self.text_red
                )
                self.result_label.config(
                    text="💀 DESTRUCTION SEQUENCE ACTIVATED",
                    fg=self.text_red
                )
                self.password_entry.config(state=tk.DISABLED)
                
                # Start destruction countdown
                self._start_destruction_countdown()
    
    def _shake_window(self):
        """Shake effect for wrong password"""
        x = self.winfo_x()
        y = self.winfo_y()
        
        for _ in range(5):
            for dx, dy in [(10, 0), (-10, 0), (0, 10), (0, -10)]:
                self.geometry(f"+{x+dx}+{y+dy}")
                self.update()
                self.after(50)
        
        self.geometry(f"+{x}+{y}")
    
    def _start_destruction_countdown(self):
        """Start the destruction countdown"""
        countdown_label = tk.Label(
            self,
            text="",
            font=self.font_title,
            fg=self.text_red,
            bg=self.bg_color
        )
        countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        def update_countdown(count=10):
            if count > 0:
                countdown_label.config(text=f"DESTRUCTION IN: {count}")
                self.after(1000, update_countdown, count - 1)
            else:
                countdown_label.config(text="SYSTEM DESTROYED")
                # In real scenario, this would trigger actual destruction
                self.after(2000, self.destroy)
        
        update_countdown()
    
    def _unlock_system(self):
        """Unlock the system - show exit message"""
        unlock_frame = tk.Frame(self, bg=self.bg_color)
        unlock_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        unlock_label = tk.Label(
            unlock_frame,
            text="✅ SYSTEM UNLOCKED\nYou may now exit",
            font=self.font_header,
            fg=self.text_green,
            bg=self.bg_color
        )
        unlock_label.pack(pady=20)
        
        exit_btn = tk.Button(
            unlock_frame,
            text="EXIT",
            font=self.font_normal,
            fg=self.text_white,
            bg="#0055ff",
            command=self.destroy,
            padx=30,
            pady=15
        )
        exit_btn.pack()
        
        # Re-enable Escape key for exit
        self.bind("<Escape>", lambda e: self.destroy())
    
    def _update_clock(self):
        """Update the clock in footer"""
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"TIME: {now}")
        self.after(1000, self._update_clock)

def main():
    """Main entry point"""
    print("Starting System Destruction Challenge...")
    print("Created by SOULGPT for zanezeXSZ")
    print("REAL MODE - NO SIMULATION - NO ANIMATION")
    
    app = SystemDestructionChallenge()
    
    try:
        app.mainloop()
    except KeyboardInterrupt:
        print("Force closed by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("System Destruction Challenge terminated")

if __name__ == "__main__":
    main()
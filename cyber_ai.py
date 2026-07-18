import tkinter as tk
from tkinter import scrolledtext, Menu
import subprocess
import threading
import os

# --- إعدادات المسار (هذا هو المفتاح) ---
# سنقوم بتحديد المسار الذي يوجد فيه الملف يدوياً لضمان أنه يعمل دائماً
PROJECT_PATH = "/home/kali/cyber_project"

class CyberApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cyber Operations Pro")
        self.geometry("750x650")
        self.configure(bg="#2c3e50")

        self.output_area = scrolledtext.ScrolledText(self, width=85, height=15, bg="black", fg="lime", font=("Consolas", 10))
        self.output_area.pack(pady=10)
        
        self.entry = tk.Entry(self, width=80)
        self.entry.pack(pady=5)

        btn_frame = tk.Frame(self, bg="#2c3e50")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start Tunnel", command=self.run_tunnel, bg="#3498db", fg="white", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Net Scan", command=self.run_scan, bg="#3498db", fg="white", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Execute", command=self.process_input, bg="#e67e22", fg="white", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Exit", command=self.destroy, bg="#e74c3c", fg="white", width=15).pack(side=tk.LEFT, padx=5)

    def _run_cmd(self, cmd):
        try:
            # نغير المسار أولاً إلى مجلد المشروع لضمان العثور على الملفات
            os.chdir(PROJECT_PATH)
            # تنفيذ الأمر
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            self.output_area.insert(tk.END, result + "\n")
        except Exception as e:
            self.output_area.insert(tk.END, f">>> [ERROR] {str(e)}\n")

    def process_input(self):
        cmd = self.entry.get()
        if not cmd: return
        self.output_area.insert(tk.END, f">>> [EXEC] {cmd}\n")
        threading.Thread(target=self._run_cmd, args=(cmd,), daemon=True).start()
        self.entry.delete(0, tk.END)

    def run_tunnel(self):
        self.output_area.insert(tk.END, ">>> [SYSTEM] Starting Tunnel...\n")
        # تنفيذ الأمر من داخل المسار المعتمد
        threading.Thread(target=self._run_cmd, args=("bash start.sh",), daemon=True).start()
    
    def run_scan(self):
        self.output_area.insert(tk.END, ">>> [SYSTEM] Running scan...\n")
        threading.Thread(target=self._run_cmd, args=("ip addr",), daemon=True).start()

if __name__ == "__main__":
    app = CyberApp()
    app.mainloop()

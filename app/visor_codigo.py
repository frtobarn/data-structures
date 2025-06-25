import tkinter as tk
from tkinter import scrolledtext

class CodeViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.current_file = None

        # Área de texto con scroll horizontal y vertical
        self.txt = scrolledtext.ScrolledText(self, wrap="none", font=("Courier", 11))
        self.txt.pack(expand=True, fill="both")

    def load(self, file_path):
        self.current_file = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        self.txt.config(state="normal")
        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", code)
        self.txt.config(state="disabled")

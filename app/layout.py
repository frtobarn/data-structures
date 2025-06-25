import tkinter as tk
from tkinter import ttk, messagebox
import os

from .visor_pdf    import PDFViewer
from .visor_codigo import CodeViewer
from .heap_demo    import HeapDemo

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Layout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ——— Menú superior ———
        menu = tk.Frame(self, height=50)
        menu.pack(side="top", fill="x")
        tk.Label(menu, text="Estructuras:").pack(side="left", padx=5)
        self.combo = ttk.Combobox(menu, values=["Heaps (Montículo de Prioridad)"])
        self.combo.current(0)
        self.combo.pack(side="left")
        btn_cargar = tk.Button(menu, text="Cargar ejemplo", command=self._cargar_ejemplo)
        btn_cargar.pack(side="left", padx=5)

        # ——— Paneles ———
        panes = tk.PanedWindow(self, orient="horizontal", sashwidth=5, sashrelief="raised")
        panes.pack(expand=True, fill="both")
        self.pdf_frame  = tk.Frame(panes); panes.add(self.pdf_frame,  minsize=300)
        self.impl_frame = tk.Frame(panes); panes.add(self.impl_frame, minsize=300)

        # ——— Visores iniciales ———
        self.pdf_viewer  = PDFViewer(self.pdf_frame)
        self.pdf_viewer.pack(expand=True, fill="both")
        self.code_viewer = CodeViewer(self.impl_frame)
        self.code_viewer.pack(expand=True, fill="both")

        # ——— Demo interactivo ———
        self.demo = HeapDemo(self.impl_frame)
        self.demo.pack(expand=True, fill="both", pady=(5,40))

        # ——— Botón modal ———
        footer = tk.Frame(self.impl_frame)
        footer.pack(side="bottom", fill="x")
        self.btn_modal = tk.Button(footer, text="Ver código completo", state="disabled",
                                   command=self._show_modal)
        self.btn_modal.pack()

    def _cargar_ejemplo(self):
        # Rutas absolutas
        pdf_path  = os.path.join(BASE, "assets", "requisitos",  "Heaps.pdf")
        code_path = os.path.join(BASE, "assets", "ejemplos_codigo", "Heaps.py")

        # Carga PDF y código
        try:
            self.pdf_viewer.load(pdf_path)
            self.code_viewer.load(code_path)
        except Exception as e:
            messagebox.showerror("Error al cargar ejemplo", str(e))
            return

        # Reinicia el demo interactivo (limpia estado anterior)
        self.demo.reset()  
        self.btn_modal.config(state="normal")

    def _show_modal(self):
        cf = self.code_viewer.current_file
        if not cf:
            messagebox.showwarning("Atención", "No hay código cargado")
            return

        modal = tk.Toplevel(self)
        modal.title("Código completo")
        modal.geometry("800x600")
        viewer = CodeViewer(modal)
        viewer.pack(expand=True, fill="both")
        viewer.load(cf)

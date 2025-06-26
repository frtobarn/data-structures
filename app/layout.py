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

        # Mapeo de estructuras de datos disponibles
        self.data_structures = {
            "Heaps": {"pdf": "Heaps.pdf", "code": "Heaps.py"},
            "Listas": {"pdf": "Listas.pdf", "code": "Listas.py"},
            "Listas Enlazadas": {"pdf": "Listas Enlazadas.pdf", "code": "Listas Enlazadas.py"},
            "Pilas": {"pdf": "Pilas.pdf", "code": "Pilas.py"},
            "Colas": {"pdf": "Colas.pdf", "code": "Colas.py"},
            "Matrices": {"pdf": "Matrices.pdf", "code": "Matrices.py"},
            "Estructuras Secuenciales": {"pdf": "Estructuras secuenciales.pdf", "code": "Estructuras secuenciales.py"},
            "Árboles Binarios": {"pdf": "Binary Search Trees.pdf", "code": "Binary_Search_Trees.py"},
            "Árboles Completos": {"pdf": "Full trees.pdf", "code": "Full_trees.py"},
            "Árboles AVL (Insert)": {"pdf": "AVL Trees insert -rotate.pdf", "code": "AVL_Trees_insert.py"},
            "Árboles AVL (Delete)": {"pdf": "AVL Trees delete.pdf", "code": "AVL_Trees_delete.py"},
            "HeapSort": {"pdf": "HeapSort.pdf", "code": "HeapSort.py"}
        }

        # ——— Menú superior ———
        menu = tk.Frame(self, height=50)
        menu.pack(side="top", fill="x")
        tk.Label(menu, text="Estructuras de Datos:").pack(side="left", padx=5)
        
        # Frame para los botones con scroll horizontal
        buttons_frame = tk.Frame(menu)
        buttons_frame.pack(side="left", fill="x", expand=True)
        
        # Crear botones para cada estructura
        for i, (name, files) in enumerate(self.data_structures.items()):
            btn = tk.Button(buttons_frame, text=name, 
                          command=lambda n=name, f=files: self._cargar_estructura(n, f))
            btn.pack(side="left", padx=2, pady=2)

        # ——— Paneles ———
        panes = tk.PanedWindow(self, orient="horizontal", sashwidth=5, sashrelief="raised")
        panes.pack(expand=True, fill="both")
        self.pdf_frame  = tk.Frame(panes); panes.add(self.pdf_frame,  minsize=300)
        self.impl_frame = tk.Frame(panes); panes.add(self.impl_frame, minsize=300)

        # ——— Visores iniciales ———
        self.pdf_container = tk.Frame(self.pdf_frame)
        self.pdf_container.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        self.pdf_viewer  = PDFViewer(self.pdf_container)
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

    def _cargar_estructura(self, name, files):
        """Carga una estructura de datos específica."""
        # Rutas absolutas
        pdf_path  = os.path.join(BASE, "assets", "requisitos", files["pdf"])
        code_path = os.path.join(BASE, "assets", "ejemplos_codigo", files["code"])

        # Carga PDF y código
        try:
            self.pdf_viewer.load(pdf_path)
            self.code_viewer.load(code_path)
        except Exception as e:
            messagebox.showerror("Error al cargar estructura", f"Error cargando {name}: {str(e)}")
            return

        # Reinicia el demo interactivo (limpia estado anterior)
        self.demo.reset()  
        self.btn_modal.config(state="normal")

    def _cargar_ejemplo(self):
        """Método legacy - ahora usa _cargar_estructura"""
        self._cargar_estructura("Heaps", self.data_structures["Heaps"])

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

import tkinter as tk
from tkinter import ttk, messagebox
import os

from .visor_pdf    import PDFViewer
from .visor_codigo import CodeViewer
from .demo_manager import DemoManager

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Layout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)  

        # Mapeo de estructuras de datos disponibles
        self.data_structures = {
            "Estructuras Secuenciales": {"pdf": "Estructuras secuenciales.pdf", "code": "Estructuras secuenciales.py"},
            "Listas": {"pdf": "Listas.pdf", "code": "Listas.py"},
            "Matrices": {"pdf": "Matrices.pdf", "code": "Matrices.py"},
            "Listas Enlazadas": {"pdf": "Listas Enlazadas.pdf", "code": "Listas Enlazadas.py"},
            "Pilas": {"pdf": "Pilas.pdf", "code": "Pilas.py"},
            "Colas": {"pdf": "Colas.pdf", "code": "Colas.py"},
            "Hash": {"pdf": "Hash.pdf", "code": "Hash.py"},
            "Heaps": {"pdf": "Heaps.pdf", "code": "Heaps.py"},
            "Árboles Binarios": {"pdf": "Binary Search Trees.pdf", "code": "Binary_Search_Trees.py"},
            "Árboles Completos": {"pdf": "Full trees.pdf", "code": "Full_trees.py"},
            "Árboles AVL": {"pdf": "AVL Trees insert -rotate.pdf", "code": "AVL_Trees_insert.py"},
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

        # Panel derecho: solo demo (sin code_viewer)
        self.demo_manager = DemoManager(self.impl_frame)
        self.demo_manager.place(relx=0, rely=0, relwidth=1, relheight=0.93)

        # ——— Botón modal ———
        footer = tk.Frame(self.impl_frame)
        footer.place(relx=0, rely=0.93, relwidth=1, relheight=0.07)
        self.btn_modal = tk.Button(footer, text="Ver código completo", state="disabled",
                                   command=self._show_modal)
        self.btn_modal.pack()

    def _cargar_estructura(self, name, files):
        """Carga una estructura de datos específica."""
        # Rutas absolutas
        pdf_path  = os.path.join(BASE, "assets", "requisitos", files["pdf"])

        # Carga PDF
        try:
            self.pdf_viewer.load(pdf_path)
        except Exception as e:
            messagebox.showerror("Error al cargar estructura", f"Error cargando {name}: {str(e)}")
            return

        # Cambiar al demo correspondiente
        self.demo_manager.show_demo(name)
        self.btn_modal.config(state="normal")

    def _cargar_ejemplo(self):
        """Método legacy - ahora usa _cargar_estructura"""
        self._cargar_estructura("Heaps", self.data_structures["Heaps"])

    def _show_modal(self):
        # Obtener la estructura actualmente seleccionada
        current_structure = None
        for name, files in self.data_structures.items():
            # Verificar si el PDF actual corresponde a esta estructura
            try:
                current_pdf = os.path.basename(self.pdf_viewer.doc.name if self.pdf_viewer.doc else "")
                if current_pdf == files["pdf"]:
                    current_structure = name
                    break
            except:
                pass
        
        if not current_structure:
            messagebox.showwarning("Atención", "No hay estructura cargada")
            return

        # Cargar el código de la estructura actual
        code_path = os.path.join(BASE, "assets", "ejemplos_codigo", self.data_structures[current_structure]["code"])
        
        if not os.path.exists(code_path):
            messagebox.showerror("Error", f"No se encontró el archivo de código: {code_path}")
            return

        modal = tk.Toplevel(self)
        modal.title(f"Código completo - {current_structure}")
        modal.geometry("800x600")
        viewer = CodeViewer(modal)
        viewer.pack(expand=True, fill="both")
        viewer.load(code_path)



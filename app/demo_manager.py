import tkinter as tk
from .heap_demo import HeapDemo
from .listas_demo import ListasDemo
from .listas_enlazadas_demo import ListasEnlazadasDemo
from .arbol_binario_completo_demo import ArbolBinarioCompletoDemo
from .arbol_binario_demo import ArbolBinarioDemo
from .arbol_avl_demo import ArbolAVLDemo
from .heapsort_demo import HeapSortDemo
from .pilas_demo import PilasDemo
from .colas_demo import ColasDemo
from .matrices_demo import MatricesDemo
from .estructuras_secuenciales_demo import EstructurasSecuencialesDemo

class DemoManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.current_demo = None
        self.demo_widgets = {}
        
        # Mapeo de estructuras a sus demos correspondientes
        self.demo_mapping = {
            "Heaps": HeapDemo,
            "Listas": ListasDemo,
            "Listas Enlazadas": ListasEnlazadasDemo,
            "Árboles Binarios": ArbolBinarioDemo,
            "Árboles Completos": ArbolBinarioCompletoDemo,
            "Árboles AVL (Insert)": ArbolAVLDemo,
            "HeapSort": HeapSortDemo,
            "Pilas": PilasDemo,
            "Colas": ColasDemo,
            "Matrices": MatricesDemo,
            "Estructuras Secuenciales": EstructurasSecuencialesDemo,
            # Agregar más demos aquí conforme se creen
            # "Colas": ColasDemo,
            # etc.
        }
        
        # Frame placeholder para el demo actual
        self.demo_frame = tk.Frame(self)
        self.demo_frame.pack(expand=True, fill="both")
        
        # Mostrar demo por defecto (Heaps)
        self.show_demo("Heaps")
    
    def show_demo(self, structure_name):
        """Cambia al demo correspondiente a la estructura seleccionada."""
        # Limpiar demo actual
        if self.current_demo:
            self.current_demo.pack_forget()
        
        # Crear nuevo demo si no existe
        if structure_name not in self.demo_widgets:
            if structure_name in self.demo_mapping:
                demo_class = self.demo_mapping[structure_name]
                self.demo_widgets[structure_name] = demo_class(self.demo_frame)
            else:
                # Demo placeholder para estructuras sin demo aún
                self.demo_widgets[structure_name] = self._create_placeholder_demo(structure_name)
        
        # Mostrar el demo
        self.current_demo = self.demo_widgets[structure_name]
        self.current_demo.pack(expand=True, fill="both", pady=(5, 40))
        
        # Reiniciar el demo
        if hasattr(self.current_demo, 'reset'):
            self.current_demo.reset()
    
    def _create_placeholder_demo(self, structure_name):
        """Crea un demo placeholder para estructuras que aún no tienen demo."""
        placeholder = tk.Frame(self.demo_frame)
        
        tk.Label(placeholder, text=f"Demo para {structure_name}", 
                font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Label(placeholder, text="Demo interactivo en desarrollo...", 
                font=("Arial", 10)).pack(pady=10)
        
        tk.Label(placeholder, text="Por ahora, puedes ver el código de ejemplo y los requisitos.", 
                wraplength=400).pack(pady=10)
        
        return placeholder
    
    def reset(self):
        """Reinicia el demo actual."""
        if self.current_demo and hasattr(self.current_demo, 'reset'):
            self.current_demo.reset() 
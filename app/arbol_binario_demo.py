import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
from io import StringIO
from .arbol_binario import ArbolBinarioBusqueda

class ArbolBinarioDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.arbol = ArbolBinarioBusqueda()
        self.setup_ui()
        
    def setup_ui(self):
        # Título
        title_label = tk.Label(self, text="Gestor de Rutas - Indexación Eficiente de Órdenes", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Descripción
        desc_text = """Sistema de gestión de órdenes usando Árbol Binario de Búsqueda (BST) para indexación eficiente.

El BST mantiene los elementos en orden clasificado, permitiendo operaciones O(log N) para:
• INSERT <order_id>: Registrar nueva orden
• SEARCH <order_id>: Buscar orden existente  
• DELETE <order_id>: Eliminar orden cancelada/completada

Después de cada operación se muestra el recorrido in-order para verificar el orden."""
        
        desc_label = tk.Label(self, text=desc_text, justify="left", wraplength=500)
        desc_label.pack(pady=10)
        
        # Frame para controles
        controls_frame = tk.Frame(self)
        controls_frame.pack(pady=10, fill="x", padx=20)
        
        # Campo de entrada
        tk.Label(controls_frame, text="Comando:").pack(side="left", padx=(0, 5))
        self.command_var = tk.StringVar()
        self.command_entry = tk.Entry(controls_frame, textvariable=self.command_var, width=30)
        self.command_entry.pack(side="left", padx=5)
        self.command_entry.bind('<Return>', self.ejecutar_comando)
        
        # Botón ejecutar
        tk.Button(controls_frame, text="Ejecutar", command=self.ejecutar_comando).pack(side="left", padx=5)
        
        # Botón limpiar
        tk.Button(controls_frame, text="Limpiar", command=self.limpiar_arbol).pack(side="left", padx=5)
        
        # Frame para casos de prueba
        test_cases_frame = tk.Frame(self)
        test_cases_frame.pack(pady=10, fill="x", padx=20)
        
        tk.Label(test_cases_frame, text="Casos de Prueba:", font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Caso 1: Construcción básica
        case1_frame = tk.Frame(test_cases_frame)
        case1_frame.pack(fill="x", pady=5)
        tk.Label(case1_frame, text="Construcción:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        case1_buttons = [
            ("INSERT 50", "INSERT 50"),
            ("INSERT 30", "INSERT 30"), 
            ("INSERT 70", "INSERT 70"),
            ("INSERT 20", "INSERT 20")
        ]
        
        for text, command in case1_buttons:
            btn = tk.Button(case1_frame, text=text, 
                          command=lambda cmd=command: self.ejecutar_ejemplo(cmd))
            btn.pack(side="left", padx=2, pady=2)
        
        # Caso 2: Operaciones mixtas
        case2_frame = tk.Frame(test_cases_frame)
        case2_frame.pack(fill="x", pady=5)
        tk.Label(case2_frame, text="Operaciones:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        case2_buttons = [
            ("SEARCH 30", "SEARCH 30"),
            ("SEARCH 90", "SEARCH 90"),
            ("DELETE 30", "DELETE 30")
        ]
        
        for text, command in case2_buttons:
            btn = tk.Button(case2_frame, text=text, 
                          command=lambda cmd=command: self.ejecutar_ejemplo(cmd))
            btn.pack(side="left", padx=2, pady=2)
        
        # Área de salida
        output_frame = tk.Frame(self)
        output_frame.pack(pady=10, fill="both", expand=True, padx=20)
        
        tk.Label(output_frame, text="Salida:", font=("Arial", 12, "bold")).pack(anchor="w")
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15, width=60)
        self.output_text.pack(fill="both", expand=True)
        
        # Estado del árbol
        self.status_label = tk.Label(self, text="Estado: Árbol vacío", 
                                   font=("Arial", 10, "italic"))
        self.status_label.pack(pady=5)
        
    def ejecutar_comando(self, event=None):
        comando = self.command_var.get().strip()
        if not comando:
            return
            
        self.ejecutar_ejemplo(comando)
        self.command_var.set("")
        
    def ejecutar_ejemplo(self, comando):
        try:
            parts = comando.split()
            if len(parts) < 2:
                return
                
            command = parts[0]
            key = int(parts[1])
            
            # Procesar comando individualmente
            if command == "INSERT":
                self.arbol.insert(key)
                output = self.arbol.in_order_traversal()
            elif command == "SEARCH":
                if self.arbol.search(key):
                    output = "ENCONTRADO"
                else:
                    output = "ID NO ENCONTRADO"
            elif command == "DELETE":
                if self.arbol.search(key):
                    self.arbol.delete(key)
                    output = "ELIMINADO\n" + self.arbol.in_order_traversal()
                else:
                    output = "ID NO ENCONTRADO\n" + self.arbol.in_order_traversal()
            else:
                return
            
            # Mostrar en interfaz
            self.output_text.insert(tk.END, f"Comando: {comando}\n")
            self.output_text.insert(tk.END, f"Salida: {output}\n")
            self.output_text.insert(tk.END, "-" * 50 + "\n")
            self.output_text.see(tk.END)
            
            # Actualizar estado
            self.actualizar_estado()
            
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}\n")
            self.output_text.see(tk.END)
        
    def actualizar_estado(self):
        """Actualiza el estado mostrado del árbol"""
        if self.arbol.root is None:
            self.status_label.config(text="Estado: Árbol vacío")
        else:
            traversal = self.arbol.in_order_traversal()
            self.status_label.config(text=f"Estado: {traversal}")
            
    def limpiar_arbol(self):
        """Limpia el árbol y la salida"""
        self.arbol = ArbolBinarioBusqueda()
        self.output_text.delete(1.0, tk.END)
        self.actualizar_estado()
        
    def reset(self):
        """Reinicia el demo"""
        self.limpiar_arbol() 
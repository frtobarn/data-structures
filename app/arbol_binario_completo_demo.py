import tkinter as tk
from tkinter import messagebox
from .arbol_binario_completo import ArbolBinarioCompleto

class ArbolBinarioCompletoDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # --- Título y descripción ---
        tk.Label(self, text="Demo: Flujo de Decisión WhatsApp (Árbol Binario Completo)", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
        desc = ("Simula el flujo de decisión de WhatsApp para confirmar, reprogramar o cancelar servicios.\n"
                "Ingresa una secuencia de elecciones (0 o 1) separadas por espacio.")
        tk.Label(self, text=desc, justify="left", wraplength=400).grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

        # --- Input de secuencia ---
        tk.Label(self, text="Secuencia de elecciones (ej: 1 0):").grid(row=2, column=0, columnspan=3, pady=5, sticky="w")
        self.e_sequence = tk.Entry(self, width=30)
        self.e_sequence.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5)
        self.e_sequence.insert(0, "1 0")

        # --- Botones ---
        btn_run = tk.Button(self, text="Ejecutar", command=self._run_reto)
        btn_clear = tk.Button(self, text="Limpiar", command=self._clear)
        btn_example = tk.Button(self, text="Ejemplo", command=self._load_example)
        btn_run.grid(row=4, column=0, padx=5, pady=5)
        btn_clear.grid(row=4, column=1, padx=5, pady=5)
        btn_example.grid(row=4, column=2, padx=5, pady=5)

        # --- Resultado ---
        tk.Label(self, text="Resultado:", font=("Arial", 10, "bold")).grid(row=5, column=0, columnspan=3, pady=(10,5), sticky="w")
        self.result_text = tk.Text(self, height=8, width=50, wrap="word")
        self.result_text.grid(row=6, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        # --- Casos de prueba ---
        tk.Label(self, text="Casos de prueba:", font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=3, pady=(10,5), sticky="w")
        test_frame = tk.Frame(self)
        test_frame.grid(row=8, column=0, columnspan=3, sticky="ew", padx=5)
        test_cases = [
            ("Confirmar", "0", "Servicio Confirmado"),
            ("Reprogramar", "1 0", "Servicio Reprogramado"),
            ("Cancelar", "1 1", "Servicio Cancelado"),
            ("Inválida", "2", "OPCION INVALIDA")
        ]
        for i, (name, input_val, expected) in enumerate(test_cases):
            btn = tk.Button(test_frame, text=name, command=lambda inp=input_val: self._test_case(inp))
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            test_frame.columnconfigure(i, weight=1)

        # Configurar grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

    def _run_reto(self):
        sequence = self.e_sequence.get().strip()
        if not sequence:
            messagebox.showwarning("Atención", "Por favor ingresa la secuencia de elecciones")
            return
        import io
        import sys
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sequence + '\n')
            output = io.StringIO()
            sys.stdout = output
            from .arbol_binario_completo import ArbolBinarioCompleto
            ArbolBinarioCompleto().ejecutar()
            result = output.getvalue().strip()
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", f"Entrada: {sequence}\n\nSalida:\n{result}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error ejecutando el reto: {str(e)}")
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    def _clear(self):
        self.e_sequence.delete(0, "end")
        self.result_text.delete("1.0", "end")

    def _load_example(self):
        self.e_sequence.delete(0, "end")
        self.e_sequence.insert(0, "1 0")

    def _test_case(self, input_val):
        self.e_sequence.delete(0, "end")
        self.e_sequence.insert(0, input_val)
        self._run_reto()

    def reset(self):
        self._clear()
        self._load_example() 
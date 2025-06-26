import tkinter as tk
from tkinter import messagebox
from .listas import RetoArray

class ListasDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.reto = RetoArray()

        # --- Título y descripción ---
        tk.Label(self, text="Demo: Retos de Programación Diarios", 
                font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
        
        desc = ("Andrés necesita registrar sus puntuaciones diarias durante una semana.\n"
                "Ingresa 7 puntuaciones (enteros no negativos) separadas por espacios.")
        tk.Label(self, text=desc, justify="left", wraplength=400).grid(
            row=1, column=0, columnspan=3, pady=5, sticky="w")

        # --- Input de puntuaciones ---
        tk.Label(self, text="Puntuaciones (7 números separados por espacios):").grid(
            row=2, column=0, columnspan=3, pady=5, sticky="w")
        self.e_scores = tk.Entry(self, width=50)
        self.e_scores.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5)
        self.e_scores.insert(0, "10 15 12 18 20 14 16")  # Ejemplo por defecto

        # --- Botones ---
        btn_run = tk.Button(self, text="Ejecutar Reto", command=self._run_reto)
        btn_clear = tk.Button(self, text="Limpiar", command=self._clear)
        btn_example = tk.Button(self, text="Ejemplo", command=self._load_example)
        
        btn_run.grid(row=4, column=0, padx=5, pady=5)
        btn_clear.grid(row=4, column=1, padx=5, pady=5)
        btn_example.grid(row=4, column=2, padx=5, pady=5)

        # --- Resultado ---
        tk.Label(self, text="Resultado:", font=("Arial", 10, "bold")).grid(
            row=5, column=0, columnspan=3, pady=(10,5), sticky="w")
        self.result_text = tk.Text(self, height=8, width=50, wrap="word")
        self.result_text.grid(row=6, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        # --- Casos de prueba ---
        tk.Label(self, text="Casos de prueba:", font=("Arial", 10, "bold")).grid(
            row=7, column=0, columnspan=3, pady=(10,5), sticky="w")
        
        test_frame = tk.Frame(self)
        test_frame.grid(row=8, column=0, columnspan=3, sticky="ew", padx=5)
        
        test_cases = [
            ("Caso 1", "10 15 12 18 20 14 16", "105"),
            ("Caso 2", "5 5 5 5 5 5 5", "35"),
            ("Caso 3", "0 0 0 0 0 0 0", "0"),
            ("Caso 4", "100 90 80 70 60 50 40", "490"),
            ("Error 1", "1 2 3 4 5 6", "ERROR"),
            ("Error 2", "1 2 3 4 5 6 7 8", "ERROR")
        ]
        
        for i, (name, input_val, expected) in enumerate(test_cases):
            row = i // 2
            col = i % 2
            btn = tk.Button(test_frame, text=name, 
                          command=lambda inp=input_val: self._test_case(inp))
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")
            test_frame.columnconfigure(col, weight=1)

        # Configurar grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

    def _run_reto(self):
        """Ejecuta el reto con los valores ingresados."""
        scores_input = self.e_scores.get().strip()
        if not scores_input:
            messagebox.showwarning("Atención", "Por favor ingresa las puntuaciones")
            return

        try:
            # Simular la entrada estándar
            import io
            import sys
            
            # Guardar stdin original
            old_stdin = sys.stdin
            old_stdout = sys.stdout
            
            # Crear streams temporales
            sys.stdin = io.StringIO(scores_input + '\n')
            output = io.StringIO()
            sys.stdout = output
            
            # Ejecutar el reto
            self.reto.run()
            
            # Restaurar streams originales
            result = output.getvalue().strip()
            sys.stdin = old_stdin
            sys.stdout = old_stdout
            
            # Mostrar resultado
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", f"Entrada: {scores_input}\n")
            self.result_text.insert("end", f"Salida: {result}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error ejecutando el reto: {str(e)}")

    def _clear(self):
        """Limpia el input y resultado."""
        self.e_scores.delete(0, "end")
        self.result_text.delete("1.0", "end")

    def _load_example(self):
        """Carga el ejemplo por defecto."""
        self.e_scores.delete(0, "end")
        self.e_scores.insert(0, "10 15 12 18 20 14 16")

    def _test_case(self, input_val):
        """Ejecuta un caso de prueba específico."""
        self.e_scores.delete(0, "end")
        self.e_scores.insert(0, input_val)
        self._run_reto()

    def reset(self):
        """Reinicia el demo."""
        self.reto = RetoArray()
        self._clear()
        self._load_example() 
import tkinter as tk
from tkinter import messagebox
from .heapsort import HeapSort

class HeapSortDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # --- Título y descripción ---
        tk.Label(self, text="Demo: HeapSort para Planificación de Rutas", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
        desc = ("Ordena tareas por métrica usando HeapSort.\n"
                "Ingresa tareas como ID-Métrica, separadas por espacios (ej: A-10 B-5 C-15 D-2 E-8)")
        tk.Label(self, text=desc, justify="left", wraplength=400).grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

        # --- Input de tareas ---
        tk.Label(self, text="Tareas (ej: A-10 B-5 C-15 D-2 E-8):").grid(row=2, column=0, columnspan=3, pady=5, sticky="w")
        self.e_tasks = tk.Entry(self, width=50)
        self.e_tasks.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5)
        self.e_tasks.insert(0, "A-10 B-5 C-15 D-2 E-8")

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
            ("Ejemplo 1", "A-10 B-5 C-15 D-2 E-8", "D B E A C"),
            ("Ejemplo 2", "Tarea1-0 Tarea2--5 Tarea3-10 Tarea4-0", "Tarea2 Tarea1 Tarea4 Tarea3"),
            ("Ejemplo 3", "ItemX-7 ItemY-7 ItemZ-7", "ItemX ItemY ItemZ"),
            ("Ejemplo 4", "SingleTask-42", "SingleTask"),
            ("Vacío", "", "")
        ]
        for i, (name, input_val, expected) in enumerate(test_cases):
            btn = tk.Button(test_frame, text=name, command=lambda inp=input_val: self._test_case(inp))
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            test_frame.columnconfigure(i, weight=1)

        # Configurar grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

    def _run_reto(self):
        tasks = self.e_tasks.get().strip()
        import io
        import sys
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(tasks + '\n')
            output = io.StringIO()
            sys.stdout = output
            from .heapsort import HeapSort
            HeapSort().ejecutar()
            result = output.getvalue().strip()
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", f"Entrada: {tasks}\n\nSalida:\n{result}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error ejecutando el reto: {str(e)}")
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    def _clear(self):
        self.e_tasks.delete(0, "end")
        self.result_text.delete("1.0", "end")

    def _load_example(self):
        self.e_tasks.delete(0, "end")
        self.e_tasks.insert(0, "A-10 B-5 C-15 D-2 E-8")

    def _test_case(self, input_val):
        self.e_tasks.delete(0, "end")
        self.e_tasks.insert(0, input_val)
        self._run_reto()

    def reset(self):
        self._clear()
        self._load_example() 
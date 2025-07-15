import tkinter as tk
from tkinter import messagebox
from .hash import RetoHashEnvios

class HashDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.reto = RetoHashEnvios()

        # --- Título y descripción ---
        tk.Label(self, text="Demo: Gestión de envíos con Hash Table", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
        desc = ("Simula el registro y consulta de envíos usando una tabla hash.\n"
                "Comandos:\n"
                "REGISTER <id> <estado>   - Registra o actualiza un envío\n"
                "STATUS <id>              - Consulta el estado de un envío\n"
                "CANCEL <id>              - Elimina un envío\n"
                "COUNT                    - Muestra el total de envíos\n"
                "END                      - Finaliza la simulación")
        tk.Label(self, text=desc, justify="left", wraplength=400).grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

        # --- Input de comandos ---
        tk.Label(self, text="Comandos (uno por línea):").grid(row=2, column=0, columnspan=3, pady=5, sticky="w")
        self.txt_commands = tk.Text(self, height=7, width=50)
        self.txt_commands.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5)
        self.txt_commands.insert("1.0", "REGISTER X123 Enviado\nREGISTER Y456 En preparación\nSTATUS X123\nCOUNT\nCANCEL X123\nSTATUS X123\nCOUNT\nEND")

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
            ("Registrar y consultar", "REGISTER X123 Enviado\nSTATUS X123\nEND"),
            ("Actualizar estado", "REGISTER X123 Enviado\nREGISTER X123 Entregado\nSTATUS X123\nEND"),
            ("Eliminar", "REGISTER X123 Enviado\nCANCEL X123\nSTATUS X123\nEND"),
            ("Contar", "REGISTER X123 Enviado\nREGISTER Y456 En preparación\nCOUNT\nEND"),
            ("No encontrado", "STATUS Z999\nEND")
        ]
        for i, (name, input_val) in enumerate(test_cases):
            btn = tk.Button(test_frame, text=name, command=lambda inp=input_val: self._test_case(inp))
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            test_frame.columnconfigure(i, weight=1)

        # Configurar grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)

    def _run_reto(self):
        commands = self.txt_commands.get("1.0", "end").strip()
        if not commands:
            messagebox.showwarning("Atención", "Por favor ingresa los comandos")
            return
        import io
        import sys
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(commands + '\n')
            output = io.StringIO()
            sys.stdout = output
            self.reto = RetoHashEnvios()  # Reiniciar para cada ejecución
            self.reto.run()
            result = output.getvalue().strip()
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", f"Entrada:\n{commands}\n\nSalida:\n{result}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error ejecutando el reto: {str(e)}")
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    def _clear(self):
        self.txt_commands.delete("1.0", "end")
        self.result_text.delete("1.0", "end")

    def _load_example(self):
        self.txt_commands.delete("1.0", "end")
        self.txt_commands.insert("1.0", "REGISTER X123 Enviado\nREGISTER Y456 En preparación\nSTATUS X123\nCOUNT\nCANCEL X123\nSTATUS X123\nCOUNT\nEND")

    def _test_case(self, input_val):
        self.txt_commands.delete("1.0", "end")
        self.txt_commands.insert("1.0", input_val)
        self._run_reto()

    def reset(self):
        self._clear()
        self._load_example() 
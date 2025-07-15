import tkinter as tk
from tkinter import messagebox
from .monticulos import Monticulos

class HeapDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.monticulos = Monticulos()

        # --- Título y descripción ---
        tk.Label(self, text="Demo: Gestión de tareas con Heap (Montículo)", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=5)
        desc = ("Simula la gestión de tareas por prioridad usando un heap mínimo.\n"
                "Comandos disponibles:\n"
                "- ADD: Agrega una tarea con ID y prioridad\n"
                "- DISPATCH: Atiende la tarea de mayor prioridad (menor número)\n"
                "- COUNT: Muestra el número de tareas pendientes\n"
                "\nEjemplo: ID = T1, Prioridad = 5")
        tk.Label(self, text=desc, justify="left", wraplength=400).grid(row=1, column=0, columnspan=3, pady=5, sticky="w")

        # --- Inputs ---
        tk.Label(self, text="ID:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.e_id   = tk.Entry(self);  self.e_id.grid(row=2, column=1, sticky="we")
        tk.Label(self, text="Prioridad:").grid(row=3, column=0, padx=5, pady=2, sticky="e")
        self.e_prio = tk.Entry(self);  self.e_prio.grid(row=3, column=1, sticky="we")

        # --- Botones ---
        btn_add      = tk.Button(self, text="ADD",      command=self._add)
        btn_dispatch = tk.Button(self, text="DISPATCH", command=self._dispatch)
        btn_count    = tk.Button(self, text="COUNT",    command=self._count)
        btn_add.grid     (row=2, column=2, padx=5)
        btn_dispatch.grid(row=3, column=2, padx=5)
        btn_count.grid   (row=4, column=2, padx=5, pady=(0,5))

        btn_clear = tk.Button(self, text="Limpiar", command=self._clear)
        btn_example = tk.Button(self, text="Ejemplo", command=self._load_example)
        btn_clear.grid(row=4, column=0, padx=5, pady=5)
        btn_example.grid(row=4, column=1, padx=5, pady=5)

        # --- Resultado ---
        tk.Label(self, text="Tareas en el heap:", font=("Arial", 10, "bold")).grid(row=5, column=0, columnspan=3, pady=(10,5), sticky="w")
        self.lst = tk.Listbox(self)
        self.lst.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        # --- Casos de prueba ---
        tk.Label(self, text="Casos de prueba:", font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=3, pady=(10,5), sticky="w")
        test_frame = tk.Frame(self)
        test_frame.grid(row=8, column=0, columnspan=3, sticky="ew", padx=5)
        test_cases = [
            ("Agregar y contar", [ ("T1", 5), ("T2", 2), ("T3", 8) ]),
            ("Despachar", [ ("T1", 5), ("T2", 2), ("T3", 8), "DISPATCH" ]),
            ("Vacío", [ "DISPATCH" ]),
        ]
        for i, (name, actions) in enumerate(test_cases):
            btn = tk.Button(test_frame, text=name, command=lambda acts=actions: self._test_case(acts))
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            test_frame.columnconfigure(i, weight=1)

        # Haz el grid expansible
        self.columnconfigure(1, weight=1)
        self.rowconfigure(6, weight=1)

    def _refresh(self):
        data = sorted(self.monticulos.heap)
        self.lst.delete(0, "end")
        for prio, tid in data:
            self.lst.insert("end", f"{tid} (prio={prio})")

    def _add(self):
        tid = self.e_id.get().strip()
        try:
            prio = int(self.e_prio.get())
        except ValueError:
            messagebox.showerror("Error", "Prioridad debe ser un entero")
            return
        self.monticulos.insertTask(tid, prio)
        self._refresh()

    def _dispatch(self):
        res = self.monticulos.extractMinTask()
        if res:
            tid, prio = res
            messagebox.showinfo("Despachado", f"ID: {tid}, Prioridad: {prio}")
        else:
            messagebox.showwarning("Atención", "MONTICULO VACIO")
        self._refresh()

    def _count(self):
        cnt = self.monticulos.getTaskCount()
        messagebox.showinfo("COUNT", f"Tareas pendientes: {cnt}")

    def _clear(self):
        self.e_id.delete(0, "end")
        self.e_prio.delete(0, "end")
        self.lst.delete(0, "end")
        self.monticulos = Monticulos()

    def _load_example(self):
        self._clear()
        # Ejemplo: T1(5), T2(2), T3(8)
        for tid, prio in [("T1", 5), ("T2", 2), ("T3", 8)]:
            self.e_id.insert(0, tid)
            self.e_prio.insert(0, str(prio))
            self._add()
            self.e_id.delete(0, "end")
            self.e_prio.delete(0, "end")

    def _test_case(self, actions):
        self._clear()
        for act in actions:
            if isinstance(act, tuple):
                tid, prio = act
                self.e_id.insert(0, tid)
                self.e_prio.insert(0, str(prio))
                self._add()
                self.e_id.delete(0, "end")
                self.e_prio.delete(0, "end")
            elif act == "DISPATCH":
                self._dispatch()
            elif act == "COUNT":
                self._count()

    def reset(self):
        self._clear()
        self._load_example()

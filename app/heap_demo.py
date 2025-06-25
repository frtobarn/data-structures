# app/heap_demo.py
import tkinter as tk
from tkinter import messagebox
from .monticulos import Monticulos   # <- import relativo de tu clase de lógica

class HeapDemo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.monticulos = Monticulos()   # <- instancias la clase, no el módulo

        # --- Inputs ---
        tk.Label(self, text="ID:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.e_id   = tk.Entry(self);  self.e_id.grid(row=0, column=1, sticky="we")
        tk.Label(self, text="Prioridad:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.e_prio = tk.Entry(self);  self.e_prio.grid(row=1, column=1, sticky="we")

        # --- Botones ---
        btn_add      = tk.Button(self, text="ADD",      command=self._add)
        btn_dispatch = tk.Button(self, text="DISPATCH", command=self._dispatch)
        btn_count    = tk.Button(self, text="COUNT",    command=self._count)
        btn_add.grid     (row=0, column=2, padx=5)
        btn_dispatch.grid(row=1, column=2, padx=5)
        btn_count.grid   (row=2, column=2, padx=5, pady=(0,5))

        # --- Listbox ---
        self.lst = tk.Listbox(self)
        self.lst.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        # Haz el grid expansible
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)

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
    
    def reset(self):
        # Crea una nueva instancia limpia de Monticulos
        self.monticulos = Monticulos()
        # Limpia entradas y listbox
        self.e_id.delete(0, "end")
        self.e_prio.delete(0, "end")
        self.lst.delete(0, "end")

import tkinter as tk
from PIL import Image, ImageTk
import fitz  # PyMuPDF

class PDFViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # --- Canvas donde se mostrará la página ---
        self.canvas = tk.Canvas(self, bg="lightgray")
        self.canvas.pack(side="top", expand=True, fill="both")

        # Scrollbars
        self.v_scroll = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.v_scroll.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.v_scroll.set)
        # self.h_scroll = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        # self.h_scroll.pack(side="bottom", fill="x")
        # self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        # --- Barra de navegación y zoom ---
        ctrl = tk.Frame(self)
        ctrl.pack(side="bottom", fill="x", pady=5)

        # Botones Anterior / Siguiente
        tk.Button(ctrl, text="« Anterior", command=self._prev).pack(side="left", padx=5)
        tk.Button(ctrl, text="Siguiente »", command=self._next).pack(side="left")

        # Slider de Zoom
        tk.Label(ctrl, text="Zoom:").pack(side="left", padx=(20,0))
        self.zoom_scale = tk.Scale(
        ctrl,
        from_=50,      # zoom mínimo 50%
        to=200,        # zoom máximo 100%
        orient="horizontal",
        length=200,
        label="Zoom (%)",
        command=self._on_zoom_change
        )
        self.zoom_scale.set(100)   # Valor inicial 100%
        self.zoom_scale.pack(side="left", padx=5)

        # --- Estado interno ---
        self.doc = None
        self.current = 0
        self.zoom_factor = 1.0  # 1.0 = 100%
        self.img_id = None
        self._drag_data = {"x": 0, "y": 0, "scroll_x": 0, "scroll_y": 0}

        # Eventos para paneo con mouse
        self.canvas.bind("<ButtonPress-1>", self._start_pan)
        self.canvas.bind("<B1-Motion>", self._do_pan)

    def load(self, pdf_path):
        """Carga un PDF desde disco y muestra su primera página."""
        self.doc = fitz.open(pdf_path)
        self.current = 0
        self._render_page()

    def _render_page(self):
        """Renderiza la página actual con el zoom actual."""
        if not self.doc:
            return
        page = self.doc.load_page(self.current)
        mat  = fitz.Matrix(self.zoom_factor, self.zoom_factor)
        pix  = page.get_pixmap(matrix=mat)
        img  = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.img_id = self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.config(scrollregion=(0, 0, pix.width, pix.height))
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def _next(self):
        if self.doc and self.current < self.doc.page_count - 1:
            self.current += 1
            self._render_page()

    def _prev(self):
        if self.doc and self.current > 0:
            self.current -= 1
            self._render_page()

    def _on_zoom_change(self, val):
        """Callback del slider: ajusta el zoom y re-render."""
        # val viene como string del Scale; convertir a float
        pct = float(val)
        self.zoom_factor = pct / 100.0
        self._render_page()

    def _start_pan(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self._drag_data["scroll_x"] = self.canvas.xview()[0]
        self._drag_data["scroll_y"] = self.canvas.yview()[0]

    def _do_pan(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        # Ajusta el scroll proporcionalmente
        self.canvas.xview_moveto(max(0, min(1, self._drag_data["scroll_x"] - dx/width)))
        self.canvas.yview_moveto(max(0, min(1, self._drag_data["scroll_y"] - dy/height)))

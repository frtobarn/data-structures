import tkinter as tk
from PIL import Image, ImageTk
import fitz  # PyMuPDF

class PDFViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # --- Label donde se mostrará la página ---
        self.label = tk.Label(self, bg="lightgray")
        self.label.pack(expand=True, fill="both")

        # --- Barra de navegación y zoom ---
        ctrl = tk.Frame(self)
        ctrl.pack(fill="x", pady=5)

        # Botones Anterior / Siguiente
        tk.Button(ctrl, text="« Anterior", command=self._prev).pack(side="left", padx=5)
        tk.Button(ctrl, text="Siguiente »", command=self._next).pack(side="left")

        # Slider de Zoom
        tk.Label(ctrl, text="Zoom:").pack(side="left", padx=(20,0))
        self.zoom_scale = tk.Scale(
        ctrl,
        from_=50,      # zoom mínimo 50%
        to=100,        # zoom máximo 100%
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
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo

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

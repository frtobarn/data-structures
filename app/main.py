import tkinter as tk
from .layout import Layout    # import relativo dentro de paquete app

def main():
    root = tk.Tk()
    root.title("Estructuras de Datos")
    # Maximizar ventana
    try:
        root.state('zoomed')         # Windows
    except tk.TclError:
        root.attributes('-fullscreen', True)  # Mac/Linux

    # Instanciar el layout principal
    Layout(root).pack(expand=True, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()
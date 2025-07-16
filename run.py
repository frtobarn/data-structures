from app.main import main

import sys, os

def resource_path(relative_path):
    """Devuelve la ruta absoluta al recurso, ya sea en desarrollo o en exe."""
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

if __name__ == "__main__":
    main()
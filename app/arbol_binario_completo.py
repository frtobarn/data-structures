# Full trees (Binary Expressions)
class Node:
    def __init__(self, question=None, action=None):
        self.question = question
        self.action = action # Solo si es un nodo hoja
        self.left = None
        self.right = None
        self.is_leaf = (action is not None)

class ArbolBinarioCompleto:
    def __init__(self):
        # Define la estructura del árbol de decisión de WhatsApp
        self.root = Node("¿Desea confirmar, reprogramar o cancelar su servicio? (0: Confirmar, 1: Reprogramar/Cancelar)")
        # Nivel 1: Opciones principales
        confirm_node = Node(action="Servicio Confirmado")
        reprogram_cancel_node = Node("¿Desea reprogramar o cancelar su servicio? (0: Reprogramar, 1: Cancelar)")
        self.root.left = confirm_node
        self.root.right = reprogram_cancel_node
        # Nivel 2: Opciones de reprogramar/cancelar
        reprogram_node = Node(action="Servicio Reprogramado")
        cancel_node = Node(action="Servicio Cancelado")
        reprogram_cancel_node.left = reprogram_node
        reprogram_cancel_node.right = cancel_node

    def ejecutar(self):
        current_node = self.root
        try:
            input_sequence = input().strip().split()
        except EOFError:
            return
        choice_index = 0
        while current_node and not current_node.is_leaf:
            if choice_index >= len(input_sequence):
                print(current_node.question)
                break
            choice = input_sequence[choice_index]
            if choice == '0':
                current_node = current_node.left
            elif choice == '1':
                current_node = current_node.right
            else:
                print("OPCION INVALIDA")
                print(current_node.question)
                return
            choice_index += 1
        if current_node and current_node.is_leaf:
            print(current_node.action)
        elif current_node:
            pass
        else:
            pass

if __name__ == "__main__":
    ArbolBinarioCompleto().ejecutar() 
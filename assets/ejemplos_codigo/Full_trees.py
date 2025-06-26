# Full trees (Bynary Expressions)
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
        # Nodo raíz: Pregunta inicial
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
                # No hay más entradas, pero no se ha llegado a una hoja
                print(current_node.question) # Repetir la pregunta si no hay más entrada
                break


            choice = input_sequence[choice_index]
           
            if choice == '0':
                current_node = current_node.left
            elif choice == '1':
                current_node = current_node.right
            else:
                print("OPCION INVALIDA")
                print(current_node.question) # Repetir la pregunta
                # No avanzar en el índice de elección para que el usuario pueda reintentar
                # En este ejercicio, la entrada es una secuencia fija, así que esto podría ser un error fatal.
                # Para el propósito del ejercicio, si la entrada es inválida, se asume que la secuencia es incorrecta.
                return # Terminar si la opción es inválida en una secuencia predefinida
           
            choice_index += 1


        if current_node and current_node.is_leaf:
            print(current_node.action)
        elif current_node:
            # Si se salió del bucle porque no hay más entrada y no es hoja
            pass # Ya se imprimió la pregunta si era necesario
        else:
            # Esto no debería ocurrir si el árbol está bien formado y la entrada es válida
            pass


if __name__ == "__main__":
    ArbolBinarioCompleto().ejecutar()

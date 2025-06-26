# Clase que representa un nodo individual en la lista enlazada simple.
class Node:
    def __init__(self, value):
        # Inicializa el nodo con un valor.
        self.value = value
        # Inicializa el puntero al siguiente nodo como None.
        self.next = None

# Clase que implementa una lista enlazada simple.
class SimpleLinkedList:
    def __init__(self):
        # Inicializa la cabeza (primer nodo) y la cola (último nodo) de la lista como None.
        self.head = None
        self.tail = None

    # Método para agregar un nodo al frente de la lista.
    def pushFront(self, value):
        # Crea un nuevo nodo con el valor dado.
        new_node = Node(value)
        # Establece el 'next' del nuevo nodo para que apunte a la cabeza actual.
        new_node.next = self.head
        # Actualiza la cabeza de la lista para que sea el nuevo nodo.
        self.head = new_node
        # Si la lista estaba vacía (la cola era None), la cola también se convierte en el nuevo nodo.
        if not self.tail:
            self.tail = new_node

    # Método para agregar un nodo al final de la lista.
    def pushBack(self, value):
        # Crea un nuevo nodo con el valor dado.
        new_node = Node(value)
        # Si la lista está vacía (la cola es None), el nuevo nodo se convierte en la cabeza y la cola.
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # Si la lista no está vacía, el 'next' de la cola actual apunta al nuevo nodo.
            self.tail.next = new_node
            # Actualiza la cola de la lista para que sea el nuevo nodo.
            self.tail = new_node

    # Método para eliminar y devolver el nodo del frente de la lista.
    def popFront(self):
        # Si la lista está vacía (la cabeza es None), devuelve None.
        if not self.head:
            return None
        # Guarda el valor del nodo de la cabeza antes de eliminarlo.
        value = self.head.value
        # Mueve la cabeza al siguiente nodo en la lista.
        self.head = self.head.next
        # Si después de mover la cabeza, la cabeza se vuelve None (la lista queda vacía), la cola también se establece a None.
        if not self.head:
            self.tail = None
        # Devuelve el valor del nodo que fue eliminado.
        return value

# Lógica principal para el "Reto Lista".
class RetoLista:
    def run(self):
        # Crea una instancia de la lista enlazada simple.
        lista = SimpleLinkedList()
        # Bucle principal para leer la entrada del usuario.
        while True:
            try:
                # Lee una línea de entrada, elimina espacios en blanco al principio y al final.
                line = input().strip()
                # Si la línea es "END", sale del bucle.
                if line == "END":
                    break
                # Si la línea comienza con "PUSH_FRONT", agrega un elemento al frente.
                if line.startswith("PUSH_FRONT"):
                    # Divide la línea para obtener el valor a agregar.
                    _, value = line.split(maxsplit=1)
                    lista.pushFront(value)
                # Si la línea comienza con "PUSH_BACK", agrega un elemento al final.
                elif line.startswith("PUSH_BACK"):
                    # Divide la línea para obtener el valor a agregar.
                    _, value = line.split(maxsplit=1)
                    lista.pushBack(value)
                # Si la línea es "POP_FRONT", elimina y muestra el elemento del frente.
                elif line == "POP_FRONT":
                    # Llama al método popFront para obtener el resultado.
                    result = lista.popFront()
                    # Imprime el resultado o "LISTA VACIA" si no hay elementos.
                    print(result if result else "LISTA VACIA")
            # Maneja el error de fin de archivo (EOFError) para salir del bucle si la entrada termina inesperadamente.
            except EOFError:
                break

if __name__ == "__main__":
    RetoLista().run()
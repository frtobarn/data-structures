# Clase que representa un nodo individual en la lista enlazada simple.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Clase que implementa una lista enlazada simple.
class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def pushBack(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def popFront(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

# Lógica principal para el "Reto Lista".
class RetoLista:
    def run(self):
        lista = SimpleLinkedList()
        while True:
            try:
                line = input().strip()
                if line == "END":
                    break
                if line.startswith("PUSH_FRONT"):
                    _, value = line.split(maxsplit=1)
                    lista.pushFront(value)
                elif line.startswith("PUSH_BACK"):
                    _, value = line.split(maxsplit=1)
                    lista.pushBack(value)
                elif line == "POP_FRONT":
                    result = lista.popFront()
                    print(result if result else "LISTA VACIA")
            except EOFError:
                break

if __name__ == "__main__":
    RetoLista().run() 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key) is not None

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
        return root

    def delete(self, key):
        initial_root = self.root
        self.root = self._delete_recursive(self.root, key)
        return initial_root is not None and self.root != initial_root or (self.root is None and initial_root is not None)

    def _in_order_traversal_recursive(self, node, result):
        if node:
            self._in_order_traversal_recursive(node.left, result)
            result.append(str(node.key))
            self._in_order_traversal_recursive(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return " ".join(result)

    def ejecutar(self):
        while True:
            try:
                line = input().strip()
                if line == "END":
                    break

                parts = line.split()
                command = parts[0]
                key = int(parts[1]) if len(parts) > 1 else None

                if command == "INSERT":
                    self.insert(key)
                    print(self.in_order_traversal())
                elif command == "SEARCH":
                    if self.search(key):
                        print("ENCONTRADO")
                    else:
                        print("ID NO ENCONTRADO")
                elif command == "DELETE":
                    if self.search(key):
                        self.delete(key)
                        print("ELIMINADO")
                        print(self.in_order_traversal())
                    else:
                        print("ID NO ENCONTRADO")
                        print(self.in_order_traversal())

            except EOFError:
                break
            except Exception as e:
                pass


if __name__ == "__main__":
    ArbolBinarioBusqueda().ejecutar() 
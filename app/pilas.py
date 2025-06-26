class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

class RetoPila:
    def run(self):
        stack = Stack()
        while True:
            try:
                line = input()
                if line.strip() == "END":
                    break
                parts = line.strip().split(maxsplit=1)
                command = parts[0]

                if command == "PUSH" and len(parts) == 2:
                    stack.push(parts[1])
                elif command == "POP":
                    result = stack.pop()
                    print(result if result else "PILA VACIA")
            except Exception:
                continue

if __name__ == "__main__":
    RetoPila().run() 
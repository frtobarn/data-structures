from collections import deque

class RetoCola:
    def run(self):
        queue = deque()
        while True:
            try:
                line = input()
                if line.strip() == "END":
                    break
                parts = line.strip().split(maxsplit=1)
                command = parts[0]

                if command == "ENQUEUE" and len(parts) == 2:
                    queue.append(parts[1])
                elif command == "DEQUEUE":
                    if queue:
                        print(queue.popleft())
                    else:
                        print("COLA VACIA")
            except Exception:
                continue
if __name__ == "__main__":
    RetoCola().run()
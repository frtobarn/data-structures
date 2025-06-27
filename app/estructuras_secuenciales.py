from collections import deque

class RetoSecuencial:
    def run(self):
        back = deque()
        forward = deque()
        current = None

        while True:
            try:
                line = input().strip()
                if line == "END":
                    break
                parts = line.split(maxsplit=1)
                cmd = parts[0]

                if cmd == "VISIT" and len(parts) == 2:
                    if current:
                        back.append(current)
                    current = parts[1]
                    forward.clear()
                    print(current)

                elif cmd == "BACK":
                    if back:
                        forward.appendleft(current)
                        current = back.pop()
                        print(current)
                    else:
                        print("IGNORAR")

                elif cmd == "FORWARD":
                    if forward:
                        back.append(current)
                        current = forward.popleft()
                        print(current)
                    else:
                        print("IGNORAR")
            except Exception:
                continue

if __name__ == "__main__":
    RetoSecuencial().run() 
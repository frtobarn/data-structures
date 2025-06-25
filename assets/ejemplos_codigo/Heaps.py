import heapq


class Monticulos:
    def __init__(self):
        self.heap = [] # Usaremos la implementación de min-heap de Python (heapq)


    def insertTask(self, task_id, priority):
        # heapq es un min-heap, por lo que almacenamos (priority, task_id)
        # para que se ordene por prioridad (el menor valor de prioridad es el más alto)
        heapq.heappush(self.heap, (priority, task_id))


    def extractMinTask(self):
        if not self.heap:
            return None
        priority, task_id = heapq.heappop(self.heap)
        return (task_id, priority)


    def getTaskCount(self):
        return len(self.heap)


    def ejecutar(self):
        while True:
            try:
                line = input().strip()
                if line == "END":
                    break


                parts = line.split(maxsplit=2)
                command = parts[0]


                if command == "ADD":
                    if len(parts) > 2:
                        try:
                            task_id = parts[1]
                            priority = int(parts[2])
                            self.insertTask(task_id, priority)
                        except ValueError:
                            pass # Ignorar líneas con formato incorrecto para ADD
                elif command == "DISPATCH":
                    result = self.extractMinTask()
                    if result:
                        task_id, priority = result
                        print(f"ID: {task_id}, Prioridad: {priority}")
                    else:
                        print("MONTICULO VACIO")
                elif command == "COUNT":
                    print(self.getTaskCount())
            except EOFError:
                break
            except Exception as e:
                # print(f"Error: {e}") # For debugging
                pass


if __name__ == "__main__":
    Monticulos().ejecutar()

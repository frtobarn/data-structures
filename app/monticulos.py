# Aquí va tu clase de lógica; así no dependes de assets para importar
import heapq

class Monticulos:
    def __init__(self):
        self.heap = []

    def insertTask(self, task_id, priority):
        heapq.heappush(self.heap, (priority, task_id))

    def extractMinTask(self):
        if not self.heap:
            return None
        prio, tid = heapq.heappop(self.heap)
        return tid, prio

    def getTaskCount(self):
        return len(self.heap)

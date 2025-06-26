class HeapSort:
    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i][1] < arr[left][1]:
            largest = left
        if right < n and arr[largest][1] < arr[right][1]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def ejecutar(self):
        try:
            line = input().strip()
            if not line:
                print("")
                return
            tasks_str = line.split()
            tasks = []
            for task_s in tasks_str:
                parts = task_s.split('-')
                if len(parts) == 2:
                    task_id = parts[0]
                    try:
                        metric = int(parts[1])
                        tasks.append([task_id, metric])
                    except ValueError:
                        pass
            n = len(tasks)
            for i in range(n // 2 - 1, -1, -1):
                self._heapify(tasks, n, i)
            for i in range(n - 1, 0, -1):
                tasks[i], tasks[0] = tasks[0], tasks[i]
                self._heapify(tasks, i, 0)
            sorted_ids = [task[0] for task in tasks]
            print(" ".join(sorted_ids))
        except EOFError:
            pass
        except Exception as e:
            pass

if __name__ == "__main__":
    HeapSort().ejecutar() 
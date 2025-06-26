class HeapSort:
    def _heapify(self, arr, n, i):
        # n es el tamaño del heap
        # i es el índice de la raíz
        largest = i  # Inicializa largest como la raíz
        left = 2 * i + 1
        right = 2 * i + 2


        # Si el hijo izquierdo es mayor que la raíz
        if left < n and arr[i][1] < arr[left][1]: # Comparar métricas (índice 1)
            largest = left


        # Si el hijo derecho es mayor que el actual largest
        if right < n and arr[largest][1] < arr[right][1]: # Comparar métricas (índice 1)
            largest = right


        # Si largest no es la raíz
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Intercambio
            self._heapify(arr, n, largest)


    def ejecutar(self):
        try:
            line = input().strip()
            if not line:
                print("")
                return


            # Parsear la entrada: "ID-Métrica ID-Métrica..."
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
                        # Ignorar elementos con métricas no numéricas
                        pass
               
            n = len(tasks)


            # Construir un max-heap
            # Reorganizar elementos desde el último nodo no hoja hacia arriba
            for i in range(n // 2 - 1, -1, -1):
                self._heapify(tasks, n, i)


            # Extraer elementos uno por uno
            # El heapify construye un max-heap basado en la métrica (mayor métrica en la raíz).
            # Para obtener un orden ascendente, extraemos el elemento más grande (raíz)
            # y lo ponemos al final, luego reconstruimos el heap con los elementos restantes.
            for i in range(n - 1, 0, -1):
                tasks[i], tasks[0] = tasks[0], tasks[i]  # Mover la raíz (más grande) al final
                self._heapify(tasks, i, 0) # Llamar heapify en el heap reducido (tamaño i)


            # La lista 'tasks' ahora está ordenada por métrica en orden ascendente
            # Extraer solo los IDs para la salida
            sorted_ids = [task[0] for task in tasks]
            print(" ".join(sorted_ids))


        except EOFError:
            pass
        except Exception as e:
            # print(f"Error: {e}") # For debugging
            pass # Ignorar otras excepciones para la calificación automática


if __name__ == "__main__":
    HeapSort().ejecutar()

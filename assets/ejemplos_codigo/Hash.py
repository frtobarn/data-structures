class HashTable:
    def __init__(self, num_buckets=16):
        # Creamos un arreglo fijo de cubetas (listas)
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(self.num_buckets)]


    def _bucket_index(self, key: str) -> int:
        # Usamos la función hash de Python para distribuir, luego módulo
        return (sum(ord(c) for c in key) * 31) % self.num_buckets


    def _find_in_bucket(self, bucket: list, key: str):
        """Devuelve el índice en la cubeta o None si no existe."""
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return None


    def put(self, key: str, value: str):
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            # Actualizar valor existente
            bucket[pos] = (key, value)
        else:
            # Insertar nuevo par al final
            bucket.append((key, value))


    def get(self, key: str) -> str:
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        pos = self._find_in_bucket(bucket, key)
        return bucket[pos][1] if pos is not None else "NO ENCONTRADO"


    def remove(self, key: str):
        idx = self._bucket_index(key)
        bucket = self.buckets[idx]
        pos = self._find_in_bucket(bucket, key)
        if pos is not None:
            bucket.pop(pos)


    def count(self) -> int:
        # Suma todos los pares en cada cubeta
        total = 0
        for bucket in self.buckets:
            total += len(bucket)
        return total




class RetoHashEnvios:
    def __init__(self):
        self.table = HashTable(num_buckets=16)


    def run(self):
        while True:
            try:
                line = input().strip()
                if line == "END":
                    break


                parts = line.split(maxsplit=2)
                cmd = parts[0]


                if cmd == "REGISTER" and len(parts) == 3:
                    tracking_id, status = parts[1], parts[2]
                    self.table.put(tracking_id, status)


                elif cmd == "STATUS" and len(parts) == 2:
                    print(self.table.get(parts[1]))


                elif cmd == "CANCEL" and len(parts) == 2:
                    self.table.remove(parts[1])


                elif cmd == "COUNT":
                    print(self.table.count())


                # Líneas inválidas se ignoran
            except EOFError:
                break
            except Exception:
                pass




if __name__ == "__main__":
    RetoHashEnvios().run()
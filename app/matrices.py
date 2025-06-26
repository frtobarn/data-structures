class RetoMatriz:
    def run(self):
        try:
            n = int(input().strip())
            mat = [list(map(int, input().split())) for _ in range(n)]
            if any(len(row) != n for row in mat):
                print("ERROR")
                return

            # Transponer
            for j in range(n):
                print(" ".join(str(mat[i][j]) for i in range(n)))

            # Calcular traza
            traza = sum(mat[i][i] for i in range(n))
            print(traza)

        except Exception:
            print("ERROR")

if __name__ == "__main__":
    RetoMatriz().run() 
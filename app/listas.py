class RetoArray:
    def run(self):
        try:
            line = input()
            scores_str = line.split()
            if len(scores_str) != 7:
                print("ERROR")
                return

            scores = [int(s) for s in scores_str]
            if any(score < 0 for score in scores):
                print("ERROR")
                return

            print(sum(scores))

        except ValueError:
            print("ERROR")
        except Exception:
            print("ERROR")

if __name__ == "__main__":
    RetoArray().run() 
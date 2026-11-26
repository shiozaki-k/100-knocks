def n_print(file, n):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    for i in lines[:n]:
        print(i, end="")

n_print("popular-names.txt", 10)
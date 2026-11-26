def n_print_rev(file, n):
    with open(file, encoding="utf-8") as f:    
        lines = f.readlines()
    for line in lines[-n:]:
        print(line, end="")

n_print_rev("popular-names.txt", 10)

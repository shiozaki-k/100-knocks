with open("popular-names.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[:10]:
        line = line.replace("\t", " ")
        print(line, end="")
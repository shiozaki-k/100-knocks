with open("popular-names.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[:10]:
        sp = line.split("\t")
        print(sp[0])
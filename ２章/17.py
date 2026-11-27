with open("popular-names.txt", encoding="utf-8") as f:
    lines = f.readlines()

result = []

for line in lines:
    head = line.split("\t")[0]
    if head not in result:
        result.append(head) 

print(len(result))



with open("popular-names.txt", encoding="utf-8") as f:
    lines = f.readlines()

result = set()
for line in lines:
    result.add(line.split("\t")[0])

print(len(result))

a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = []

a = a.replace(",", "").replace(".", "")
b = a.split()
for i in range(len(b)):
  result.append(len(b[i]))

print(result)

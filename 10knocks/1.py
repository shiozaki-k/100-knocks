a = "パタトクカシーー"
result = ""

for i in range(len(a)):
  if i % 2 == 1:
    result = result + a[i]

print(result)

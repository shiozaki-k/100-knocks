a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
x = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

a = a.replace(",", "").replace(".", "")
b = a.split()

for i in range(len(b)):
  c = b[i]
  if i + 1 in x:
    result[c[0]] = i + 1
  else:
    result[c[0:2]] = i + 1

print(result)
print(result["P"])
print(result["Li"])

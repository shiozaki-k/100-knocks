def union(a, b):
  return a | b

def intersection(a, b):
  return a & b

def difference(a, b):
  return a - b

X = set(n_gram(2, "paraparaparadise"))
Y = set(n_gram(2, "paragraph"))

print(X)
print(Y)
print(union(X, Y))
print(intersection(X, Y))
print(difference(X, Y))

Z = set(["se"])
print(intersection(Z, X))
print(intersection(Z, Y))

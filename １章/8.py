def cipher(word):
  result = ""

  for i in word:
    if "a" <= i <= "z":
      i = chr(219 - ord(i))
    result += i

  return result

print(cipher("aAatT/?:;"))

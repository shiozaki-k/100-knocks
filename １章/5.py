def n_gram(n, seq):
  result = []

  for i in range(len(seq) - n + 1):
      result.append(seq[i : i + n])

  return result

a = "I am an NLPer"

char_tri_gram = n_gram(3, a)
word_bi_gram = n_gram(2, a.split())

print(char_tri_gram)
print(word_bi_gram)

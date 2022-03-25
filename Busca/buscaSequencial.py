def buscaSeq(x, proc):
  n = len(x)
  for i in range(0, n):
    if x[i] == proc:
      return i
  return -1

x = [2, 1, 4, 5, 7, 9, 10, 8, 3]
i = 0
k = buscaSeq(x, i)
if k >= 0:
  print(i, "Está na posição", k, "do vetor")
else:
  print(i, "Não se encontra no vetor")
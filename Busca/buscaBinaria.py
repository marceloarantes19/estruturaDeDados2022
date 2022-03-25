def buscaBin(x, proc):
  li = 0
  ls = len(x) - 1
  while li<=ls:
    pos = (li+ls)//2
    if proc == x[pos]:
      return pos
    elif proc < x[pos]:
      ls = pos - 1
    else:
      li = pos + 1
  return -1

x = [1, 2, 3, 4, 5, 7, 8, 9, 10]
i = 11
k = buscaBin(x, i)
if k >= 0:
  print(i, "Está na posição", k, "do vetor")
else:
  print(i, "Não se encontra no vetor")
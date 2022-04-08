def shell(self, x):
  h = 1
  n = len(x)
  while h < n:
    h = h * 3 + 1
  while h > 1:
    h = h // 3
    for i in range(h, n, h):
      atual = x[i]
      j = i - h
      while j >= 0 and atual < x[j]:
        x[j+h] = x[j]
        j = j - h
      x[j+h] = atual
  return x

x = [2, 7, 8, 1, 3, 6]
print("Fim do algoritmo -", shell(x))
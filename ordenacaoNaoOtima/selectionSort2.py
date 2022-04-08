def selection(x):
  n = len(x)
  for i in range(0, n-1):
    ordenado = True
    for j in range(i+1, n):
      if x[i]>x[j]:
        x[i], x[j] = x[j], x[i]
        ordenado = False
    if ordenado:
      return x
  return x
x = [2, 7, 8, 1, 3, 6]
print("Fim do algoritmo -", selection(x))

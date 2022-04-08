def selection(x):
  n = len(x)
  for i in range(0, n-1):
    k = i
    for j in range(i+1, n):
      if x[k]>x[j]:
        k = j
    x[i], x[k] = x[k], x[i]
  return x

x = [2, 7, 8, 1, 3, 6]
print("Fim do algoritmo -", selection(x))

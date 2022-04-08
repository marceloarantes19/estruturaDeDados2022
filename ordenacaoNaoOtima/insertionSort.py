def insertion(x):
  n = len(x)
  for i in range(1, n):
    k = x[i]
    j = i
    while j>=1 and x[j-1]>k:
      x[j] = x[j-1]
      j = j - 1
    x[j] = k
  return x

x = [2, 7, 8, 1, 3, 6]
print("Fim do algoritmo -", insertion(x))

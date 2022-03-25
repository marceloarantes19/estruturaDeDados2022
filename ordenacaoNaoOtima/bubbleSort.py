def bubble(x):
  n = len(x) - 1
  for i in range(0, n):
    for j in range(n, i, -1):
      if x[j-1] > x[j]:
        x[j-1], x[j] = x[j], x[j-1]

x = [5, 4, 3, 2, 1]
i = 0
bubble(x)
print(x)





import random
import time
def bubble(y):
  x = y[0:len(y)]
  ini = time.time()
  n = len(x)-1
  for i in range(0, n):
    for j in range(n-1, i-1, -1):
      if x[j]>x[j+1]:
        t = x[j]
        x[j] = x[j+1]
        x[j+1] = t
  fim = time.time()
  print ("Bubble:", fim - ini)
  return x

def ordena2(y):
  ini = time.time()
  x = y[0:len(y)]
  i = -1
  b = [0,0,0]
  for i in range(0, len(x)):
    b[x[i]] = b[x[i]] + 1

  for i in range(0, len(x)):
    if b[0]>0:
      x[i] = 0
      b[0] = b[0] - 1
    elif b[1]>0:
      x[i] = 1
      b[1] = b[1] - 1
    else:
      x[i] = 2
      b[2] = b[2] - 1
  fim = time.time()
  print("Outro:", (fim - ini))
  return x

x = []
for i in range(0, 100000):
  x.append(random.randint(0, 2))
  #print(random.randint(0, 2))

k = bubble(x)
l = ordena2(x)


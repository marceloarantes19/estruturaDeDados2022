x = []
i = -1
b = [0,0,0]
while True:
  i = i + 1
  v = int(input("Digite 0, 1, 2 - qualquer outro número para a repetição"))
  if v>=0 and v<3:
    x.append(v)
    b[v]=b[v]+1
  else:
    break 

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
print(x)
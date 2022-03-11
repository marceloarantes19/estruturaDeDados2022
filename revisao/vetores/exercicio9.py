x = []
while True:
  v = int(input("Digite um número (valor negativo para a entrada de Dados): "))
  if v>=0:
    x.append(v)
  else:
    break 
for i in range(0, len(x) - 1):
  for j in range(i+1, len(x)):
    if x[i] > x[j]:
      x[i], x[j] = x[j], x[i]
print(x)

# Permitir a digitação de 10 números e mostrá-los
# na ordem inversa a que foram lidos.

# 1 - Definir o vetor
v = []
l = 10
# 2 - permitir a digitação de 10 números
for i in range(0, l):
  k = int(input("digite um número: "))
  v.append(k)

# 3 - apresenta os números em ordem inversa
for i in range(l-1, -1, -1):
  print(v[i], " --- ", v[l-i-1])


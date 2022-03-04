x = [4, 5, 8, 10, 9]
print(x)
print(x[3])
print(x.pop())
print(x, 'Tamanho ', len(x))
x.append(20)
x.append(15)
print('Vetor: ',x, 'Tamanho', len(x))
y = x.pop(0)
print(y, y+1)
print(x)
for i in range(0, len(x)):
  print(i, "---", x[i])

# Foreach
for i in x:
  print(i)

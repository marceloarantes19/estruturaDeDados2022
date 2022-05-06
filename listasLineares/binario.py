from Pilha import Pilha
p = Pilha()
num = int(input('Digite um natural: '))
x = num
y = ''
while x > 0:
  p.empilha(x % 2)
  x = x // 2
while not p.pilhaVazia():
  y = y + str(p.desempilha())
print(num, ' = ', y)


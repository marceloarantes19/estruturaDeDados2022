from Pilha import Pilha
p = Pilha()
nome = input('Digite um nome: ')
ninv = ''
for i in nome:
  p.empilha(i)
while not p.pilhaVazia():
  ninv = ninv + p.desempilha()
print(nome, 'invertido é', ninv)

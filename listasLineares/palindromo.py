from Pilha import Pilha
p = Pilha()
nome = input('Digite um nome: ')
ninv = ''
for i in nome:
  p.empilha(i)
while not p.pilhaVazia():
  ninv = ninv + p.desempilha()
if nome == ninv:
  print(nome, 'É palíndromo.')
else:
  print(nome, 'Não é palíndromo.')

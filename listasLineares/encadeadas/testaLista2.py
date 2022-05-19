from Pilha import Pilha
from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
p = Pilha()
x = input('Digite um nome: ')
j = 0
for i in x:
  j = j + 1
  elem = Elemento()
  elem.setNome(i)
  elem.setChave(j)
  n = No(elem)
  l.insereNoFim(n)
print('Lista do primeiro para o último:')
l.mostraLista()
while not l.listaVazia():
  p.empilha(l.retiraNoInicio())

while not p.pilhaVazia():
  l.insereNoFim(p.desempilha())

print('Lista do Invertida:')
l.mostraLista()

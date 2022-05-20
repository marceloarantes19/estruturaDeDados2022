from PilhaEncadeada import PilhaEncadada # Já alterado para exercício 1
from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
p = PilhaEncadada()
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
  p.push(l.retiraNoInicio())

while not p.pilhaVazia():
  l.insereNoFim(p.pop())

print('Lista do Invertida:')
l.mostraLista()

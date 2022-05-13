from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = input('Digite um nome: ')
for i in x:
  elem = Elemento()
  elem.setNome(i)
  n = No(elem)
  l.insereNoInicio(n)
while not l.listaVazia():
  print(l.retiraNoInicio().getElemento().getNome())
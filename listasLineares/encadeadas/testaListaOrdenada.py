from Elemento import Elemento 
from No import No 
from Lista import Lista 
l = Lista()
x = int(input('Digite um valor: '))
while x != -1:
  elem = Elemento()
  elem.setChave(x)
  n = No(elem)
  l.insereOrdenadoChave(n)
  print("Lista ordenada")
  l.mostraLista()
  x = int(input('Digite um valor: '))
while not l.listaVazia():
  x = int(input('Digite um valor: '))
  y = l.retiraNoChave(x)
  if y != None:
    print("Retirado: ", y.getElemento().getChave())
    l.mostraLista()

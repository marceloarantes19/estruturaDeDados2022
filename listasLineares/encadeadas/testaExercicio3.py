# Programa para testar o exercício 3 - mostar a quantidade de elementos de uma lista
from Elemento import Elemento 
from No import No 
from ListaCorrecaoExercicos import Lista 
l = Lista()
x = int(input('Digite um valor de chave (digite -1 para sair): '))
while x != -1:
  y = input('Digite um nome: ')
  elem = Elemento()
  elem.setChave(x)
  elem.setNome(y)
  n = No(elem)
  l.insereNoFim(n)
  x = int(input('Digite um valor:  de chave (digite -1 para sair): '))

print('\nLista abaixo: ')
l.mostraLista()
print('Quantidade de Elementos na lista: ', l.getQtdDeElementos())
print('Quantidade de Elementos na lista: ', l.getQtdDeElementosRec(l.getCabeca().getProximo()))
# Programa para testar o exercício 3 - mostar a quantidade de elementos de uma lista
from Elemento import Elemento 
from No import No 
from ListaCorrecaoExercicos import Lista 
l = Lista()

#Testa o exercício 6
x = int(input('Digite um valor de chave (digite -1 para sair): '))
while x != -1:
  y = input('Digite um nome: ')
  p = int(input('Digite a posição de entrada na lista: '))
  elem = Elemento()
  elem.setChave(x)
  elem.setNome(y)
  n = No(elem)
  l.insereNaPosicao(n,p)
  l.mostraLista() 
  x = int(input('\nDigite um valor de chave (digite -1 para sair): '))
# Fim de Teste do Exercício 6

# Início de Teste do Exercício 7
x = int(input('Digite a posição do nó a ser retirado da lista (digite -1 para terminar): '))
while x != -1 and not l.listaVazia():
  n = l.retiraNaPosicao(x)
  if n!=None:
    print('Valor retirado:', n.getElemento().getValores())
    print('Lista atual: ')
    l.mostraLista() 
  x = int(input('Digite a posição do nó a ser retirado da lista (digite -1 para terminar): '))
# Fim de Teste do Exercício 7

# Teste do Exercício 8
print('\nLista abaixo: ')
l.mostraLista()
print('Quantidade de Elementos na lista: ', l.getQtdDeElementos())
l.limpaLista(l.getCabeca())
print('\nLista limpa: ')
l.mostraLista()
print('Quantidade de Elementos na lista: ', l.getQtdDeElementos())


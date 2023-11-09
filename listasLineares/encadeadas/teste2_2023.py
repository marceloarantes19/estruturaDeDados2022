from Elemento import Elemento
from No import No
from Lista import Lista
l = Lista()
i = int(input("Digite a chave (-1 para sair): "))
while i != -1:
  nome = input("Digite um nome: ")
  e = Elemento(i)
  e.setNome(nome)
  n = No(e)
  l.insereNoFim(n)
  print("\nMostrando a lista após a entrada de:", i)
  l.mostraLista()
  i = int(input("Digite a chave (-1 para sair): "))
while not l.listaVazia():
  x = l.retiraNoFim()
  print(x.getElemento().getValores())

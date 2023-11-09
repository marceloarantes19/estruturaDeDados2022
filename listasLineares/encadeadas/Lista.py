from Elemento import Elemento
from No import No
class Lista:
  def __init__(self):
    elemento = Elemento()
    no = No(elemento)
    self.__cabeca = no
  def getCabeca(self):
    return self.__cabeca
  def setCabeca(self, c):
    self.__cabeca = c

  # Método que verifica se a Lista está vazia
  def listaVazia(self):
    return self.getCabeca().getProximo() == None

  # Método para inserir dados no início da Lista
  def insereNoInicio(self, n): # n é um nó
    n.setProximo(self.getCabeca().getProximo())
    self.getCabeca().setProximo(n)
  
  # Método para retirar dados no início da Lista
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.getCabeca().getProximo()
      self.getCabeca().setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret

  # Método para inserir dados no fim da Lista
  def insereNoFim(self, n):
    aux = self.getCabeca()
    while aux.getProximo() != None:
      aux = aux.getProximo()
    aux.setProximo(n)

  # Método para retirar dados no fim da Lista
  def retiraNoFim(self):
    atual = None
    if not self.listaVazia():
      aux = self.getCabeca()
      atual = self.getCabeca().getProximo()
      while atual.getProximo() != None:
        aux = atual
        atual = aux.getProximo()
      aux.setProximo(None)
    return atual

  # Método para inserir dados ordenados pela chave
  def insereOrdenadoChave(self, n):
    aux = self.getCabeca()
    atual = aux.getProximo()
    while atual != None and n.getElemento().getChave()>atual.getElemento().getChave():
      aux = atual
      atual = aux.getProximo()
    n.setProximo(atual)
    aux.setProximo(n)

  # Método para retirar dados a partir da chave
  def retiraNoChave(self, v):
    atual = None
    if not self.listaVazia():
      aux = self.getCabeca()
      atual = aux.getProximo()
      while atual != None and v!=atual.getElemento().getChave():
        aux = atual
        atual = aux.getProximo()
      if atual != None:
        aux.setProximo(atual.getProximo())
        atual.setProximo(None)
    return atual

  # Método INTERATIVO para mostrar os elementos da lista
  def mostraLista(self):
    if not self.listaVazia():
      aux = self.getCabeca().getProximo()
      while aux != None:
        print(aux.getElemento().getValores())
        aux = aux.getProximo()

  # Método RECURSIVO para mostrar os elementos da lista - Exercício 4
  def mostraListaRecursivo(self, atual):
    if atual != None:
        print(atual.getElemento().getValores())
        self.mostraListaRecursivo(atual.getProximo())

  # Método RECURSIVO para mostrar os elementos da lista do último para o primeiro - Exercício 5
  def mostraListaInvertida(self, atual):
    if atual != None:
        self.mostraListaInvertida(atual.getProximo())
        print(atual.getElemento().getValores())

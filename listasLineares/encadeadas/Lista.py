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
    ret = None
    if not self.listaVazia():
      aux1 = self.getCabeca()
      aux2 = self.getCabeca().getProximo()
      while aux2.getProximo() != None:
        aux1 = aux2
        aux2 = aux2.getProximo()
      aux1.setProximo(None)
      ret = aux2
    return ret

  # Método para inserir dados ordenados pela chave
  def insereOrdenadoChave(self, n):
    aux = self.getCabeca()
    auxProx = aux.getProximo()
    while auxProx != None and n.getElemento().getChave()>auxProx.getElemento().getChave():
      aux = auxProx
      auxProx = aux.getProximo()
    n.setProximo(auxProx)
    aux.setProximo(n)

  # Método para retirar dados a partir da chave
  def retiraNoChave(self, v):
    ret = None
    if not self.listaVazia():
      aux = self.getCabeca()
      auxProx = aux.getProximo()
      while auxProx != None and v!=auxProx.getElemento().getChave():
        aux = auxProx
        auxProx = aux.getProximo()
      ret = auxProx
      if auxProx != None:
        aux.setProximo(auxProx.getProximo())
        ret.setProximo(None)
      else:
        aux.setProximo(None)
    return ret

  # Método INTERATIVO para mostrar os elementos da lista
  def mostraLista(self):
    if not self.listaVazia():
      aux = self.getCabeca().getProximo()
      while aux != None:
        print(aux.getElemento().getValores())
        aux = aux.getProximo()

  # Método RECURSIVO para mostrar os elementos da lista
  def mostraListaRecursivo(self, atual):
    if atual != None:
        print(atual.getElemento().getValores())
        self.mostraListaRecursivo(atual.getProximo())

  # Método RECURSIVO para mostrar os elementos da lista do último para o primeiro
  def mostraListaInvertida(self, atual):
    if atual != None:
        self.mostraListaInvertida(atual.getProximo())
        print(atual.getElemento().getValores())

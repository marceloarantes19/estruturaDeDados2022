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
  def listaVazia(self):
    return self.getCabeca().getProximo() == None
  def insereNoInicio(self, n): # n é um nó
    n.setProximo(self.getCabeca().getProximo())
    self.getCabeca().setProximo(n)
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.getCabeca().getProximo()
      self.getCabeca().setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret
  def insereNoFim(self, n):
    aux = self.getCabeca()
    while aux.getProximo() != None:
      aux = aux.getProximo()
    aux.setProximo(n)
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



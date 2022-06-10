from Elemento import Elemento
class NoABB:
  def __init__(self, i = Elemento()):
    self.__info = i
    self.__filhoE = None
    self.__filhoD = None
  def getInfo(self):
    return self.__info 
  def setInfo(self, i):
    self.__info = i 
  def getFilhoE(self):
    return self.__filhoE 
  def setFilhoE(self, fe):
    self.__filhoE = fe 
  def getFilhoD(self):
    return self.__filhoD 
  def setFilhoD(self, fd):
    self.__filhoD = fd
  def eFolha(self):
    return self.getFilhoE() == None and self.getFilhoD() == None
  def temDoisFilhos(self):
    return self.getFilhoE() != None and self.getFilhoD() != None
  def soTemFilhoAEsquerda(self):
    return self.getFilhoE() != None and self.getFilhoD() == None
  def soTemFilhoADireita(self):
    return self.getFilhoE() == None and self.getFilhoD() != None
  def eFilhoAEsquerda(self, n): # nó atual é filho à esquerda de n?
    return n.getFilhoE() == self
  def eFilhoADireita(self, n):  # nó atual é filho à direita de n?
    return n.getFilhoD() == self

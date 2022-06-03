from sklearn.semi_supervised import SelfTrainingClassifier
from Elemento import Elemento
from NoABB import NoABB
class ArvoreBB:
  def __init__(self):
    self.__raiz = None
  def getRaiz(self):
    return self.__raiz 
  def setRaiz(self, r):
    self.__raiz = r
  def arvoreVazia(self):
    return self.getRaiz() == None
  def insereNo(self, n = NoABB()):
    if self.arvoreVazia():
      self.setRaiz(n)
    else:
      self.insere(None, self.getRaiz(), n)
  def insere(self, pai, atual, n):
    if atual == None: # preciso inserir o nó
      if n.getInfo().getChave()<pai.getInfo().getChave():
        pai.setFilhoE(n)
      else:
        pai.setFilhoD(n)
      print("tratar")
    elif n.getInfo().getChave()<atual.getInfo().getChave():
      self.insere(atual, atual.getFilhoE(), n)
    else:
      self.insere(atual, atual.getFilhoD(), n)
  
  def visitaPreOrdem(self, n):
    if n != None:
      print(n.getInfo().getValores())
      self.visitaPreOrdem(n.getFilhoE())
      self.visitaPreOrdem(n.getFilhoD())

  def visitaEmOrdem(self, n):
    if n != None:
      self.visitaEmOrdem(n.getFilhoE())
      print(n.getInfo().getValores())
      self.visitaEmOrdem(n.getFilhoD())

  def visitaPosOrdem(self, n):
    if n != None:
      self.visitaPosOrdem(n.getFilhoE())
      self.visitaPosOrdem(n.getFilhoD())
      print(n.getInfo().getValores())
  
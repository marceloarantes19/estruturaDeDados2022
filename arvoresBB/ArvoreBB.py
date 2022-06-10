from ast import Return
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
    elif n.getInfo().getChave()<atual.getInfo().getChave():
      self.insere(atual, atual.getFilhoE(), n)
    else:
      self.insere(atual, atual.getFilhoD(), n)
  def retiraNo(self, ch):
    ret = None
    if not self.arvoreVazia():
      ret = self.retira(None, self.getRaiz(), ch)
    return ret 
  def retira(self, pai, atual, ch):
    if atual == None: # Não encontrou elemento na árvore
      return None
    elif ch < atual.getInfo().getChave(): # Procurado é menor que a chave atual
      return self.retira(atual, atual.getFilhoE(), ch)
    elif ch > atual.getInfo().getChave(): # Procurado é maior que a chave atual
      return self.retira(atual, atual.getFilhoD(), ch)
    else: # Encontrou o elemento a remover da árvore
      if not atual.temDoisFilhos():
        # Remoções triviais
        if atual.eFolha():
          if pai == None: # atual é o último nó da árvore
            self.setRaiz(None)
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(None)
          else:
            pai.setFilhoD(None)
        elif atual.soTemFilhoAEsquerda():
          if pai == None:
            self.setRaiz(atual.getFilhoE())
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(atual.getFilhoE())
          else:
            pai.setFilhoD(atual.getFilhoE())
          atual.setFilhoE(None)
        else:
          if pai == None:
            self.setRaiz(atual.getFilhoD())
          elif atual.eFilhoAEsquerda(pai):
            pai.setFilhoE(atual.getFilhoD())
          else:
            pai.setFilhoD(atual.getFilhoD())
          atual.setFilhoD(None)
        return atual
      # Remoção não trivial
      else:
        return self.simulaRemocao(atual, atual, atual.getFilhoE())
  def simulaRemocao(self, fixo, pai, atual):
    if atual.getFilhoD() != None:
      return self.simulaRemocao(fixo, atual, atual.getFilhoD())
    else:
      x = fixo.getInfo()
      fixo.setInfo(atual.getInfo())
      atual.setInfo(x)
      if fixo == pai:
        pai.setFilhoE(atual.getFilhoE())
        atual.setFilhoE(None)
      else:
        pai.setFilhoD(atual.getFilhoE())
        atual.setFilhoE(None)
      return atual
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
  def mostraArvore(self, n, niv):
    if n != None:
      sn = ""
      for i in range(0, niv):
        sn = sn +"   |"
      sn = sn + "--"
      print(sn,n.getInfo().getChave())
      self.mostraArvore(n.getFilhoE(), niv+1)
      self.mostraArvore(n.getFilhoD(), niv+1)
  # Correção dos exercícios
  # Exercício 1
  def visitaEmOrdemInversa(self, n):
    if n != None:
      self.visitaEmOrdemInversa(n.getFilhoD())
      print(n.getInfo().getValores())
      self.visitaEmOrdemInversa(n.getFilhoE())
  # Exercício 2
  def encontraNoChave(self, n, ch):
    if n != None:
      if n.getInfo().getChave() == ch:
        return n 
      elif ch < n.getInfo().getChave():
        return self.encontraNoChave(n.getFilhoE(), ch)
      else:
        return self.encontraNoChave(n.getFilhoD(), ch)
    return None
  # Exercício 3
  def qtdElem(self, n):
    #return 0 if n == None else 1 + self.qtdElem(n.getFilhoE())+ self.qtdElem(n.getFilhoD())
    if n != None:
      return 1 + self.qtdElem(n.getFilhoE()) + self.qtdElem(n.getFilhoD())
    return 0
  # Exercício 4
  def somaElem(self, n):
    if n != None:
      return n.getInfo().getChave() + self.somaElem(n.getFilhoE()) + self.somaElem(n.getFilhoD())
    return 0
  # Exercício 5
  def menorElem(self, n):
    if n != None:
      if n.getFilhoE() != None:
        return self.menorElem(n.getFilhoE())
      else:
        return n 
    return None
  # Exercício 6
  def maiorElem(self, n):
    if n != None:
      if n.getFilhoD() != None:
        return self.maiorElem(n.getFilhoD())
      else:
        return n 
    return None
  # exercicio 7
  def mostraNivelANivel(self):
    f = []
    f.append(self.getRaiz())
    while len(f) > 0:
      atual = f.pop(0)
      print(atual.getInfo().getChave())
      if atual.getFilhoE() != None:
        f.append(atual.getFilhoE())
      if atual.getFilhoD() != None:
        f.append(atual.getFilhoD())
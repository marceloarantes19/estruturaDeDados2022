from Elemento import Elemento
class No:
    def __init__(self):
        self._elemento = Elemento(None)
        self._filhoEsquerda = None
        self._filhoDireita = None
    def getFilhoEsquerda(self):
        return self._filhoEsquerda
    def setFilhoEsquerda(self, n):
        self._filhoEsquerda = n
    def setfilhoDireita(self, n):
        self._filhoDireita = n
    def getFilhoDireita(self):
        return self._filhoDireita
    def getElemento(self):
        return self._elemento
    def setElemento(self, e):
        self._elemento = e
    def eFolha(self):
        return self.getFilhoEsquerda()==None and self.getFilhoDireita()==None
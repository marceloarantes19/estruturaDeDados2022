class No:
    def __init__(self, e):
        self._elemento = e
        self._proximo = None
    def getElemento(self):
        return self._elemento
    def setElemento(self, e):
        self._elemento = e
    def getProximo(self):
        return self._proximo
    def setProximo(self, p):
        self._proximo = p
class NoDupla:
    def __init__(self, e):
        self._elemento = e
        self._anterior = None
        self._proximo = None
    def getElemento(self):
        return self._elemento
    def setElemento(self, e):
        self._elemento = e
    def getAnterior(self):
        return self._anterior
    def setAnterior(self, a):
        self._anterior = a
    def getProximo(self):
        return self._proximo
    def setProximo(self, p):
        self._proximo = p
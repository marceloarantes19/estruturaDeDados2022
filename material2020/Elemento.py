class Elemento:
    def __init__(self, v):
        self._valor = v
        self._nome = ""

    def getValor(self):
        return self._valor

    def setValor(self, v):
        self._valor = v

    def getNome(self):
        return self._nome

    def setNome(self, n):
        self._nome = n

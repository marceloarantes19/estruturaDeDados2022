from Vertice import Vertice
class Aresta:
    def __init__(self):
        self._origem = None
        self._destino = None
        self._nome = None
        self._valor = None
    def getOrigem(self):
        return self._origem
    def setOrigem(self,o):
        self._origem = o
    def getDestino(self):
        return self._destino
    def setDestino(self,d):
        self._destino = d
    def getNome(self):
        return self._nome
    def setNome(self, n):
        self._nome = n
    def getValor(self):
        return self._valor
    def setValor(self, v):
        self._valor = v
    def adcAresta(self, o, d):
        self.setOrigem(o)
        self.setDestino(d)
    def adcArestaNome(self, o, d):
        vo = Vertice()
        vd = Vertice()
        vo.setNome(o)
        vd.setNome(d)
        self.setOrigem(vo)
        self.setDestino(vd)
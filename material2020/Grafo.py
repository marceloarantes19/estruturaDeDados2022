from Vertice import Vertice
from Aresta import Aresta
class Grafo:
    def __init__(self):
        self._vertices = list()
        self._arestas = list()
    def getVertices(self):
        return self._vertices
    def setVertices(self, v):
        self._vertices = v
    def getArestas(self):
        return self._arestas
    def setArestas(self,a):
        self._arestas = a
    def existeVertice(self, v):
        return True if v in self.getVertices() else False
    def existeVerticePorNome(self, n):
        for i in self.getVertices():
            if i.getNome() == n:
                return True
        return False
    def getVerticePorNome(self, n):
        for i in self.getVertices():
            if i.getNome() == n:
                return i
        return None
    def existeAresta(self,o,d):
        for i in self.getArestas():
            if i.getOrigem() == o and i.getDestino() == d:
                return True
        return False
    def existeArestaPorNome(self,o,d):
        for i in self.getArestas():
            if i.getOrigem().getNome() == o and i.getDestino().getNome() == d:
                return True
        return False
    def adcAresta(self, o, d):
        if not self.existeVertice(o):
            self.getVertices().append(o)
        if not self.existeVertice(d):
            self.getVertices().append(d)
        if not self.existeAresta(o, d):
            a = Aresta()
            b = Aresta()
            a.setOrigem(o)
            a.setDestino(d)
            b.setOrigem(d)
            b.setDestino(o)
            self.getArestas().append(a)
            self.getArestas().append(b)
    def adcArestaPorNome(self, o, d):
        vo = None
        vd = None
        if not self.existeVerticePorNome(o):
            vo = Vertice()
            vo.setNome(o)
            self.getVertices().append(vo)
        else:
            vo = self.getVerticePorNome(o)
        if not self.existeVerticePorNome(d):
            vd = Vertice()
            vd.setNome(d)
            self.getVertices().append(vd)
        else:
            vd = self.getVerticePorNome(d)
        a = Aresta()
        b = Aresta()
        a.setOrigem(vo)
        a.setDestino(vd)
        b.setOrigem(vd)
        b.setDestino(vo)
        self.getArestas().append(a)
        self.getArestas().append(b)
    def getVizinhos(self, p):
        v = list()
        for i in self.getArestas():
            if i.getOrigem() == p:
                v.append(i.getDestino())
        return v
    def getVizinhosPorNome(self, q):
        p = self.getVerticePorNome(q)
        v = list()
        for i in self.getArestas():
            if i.getOrigem() == p:
                v.append(i.getDestino())
        return v
    def mostraGrafo(self):
        for i in self.getVertices():
            print(i.getNome())
            for j in self.getVizinhos(i):
                print("---------- ", j.getNome())


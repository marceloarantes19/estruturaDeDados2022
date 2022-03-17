from No import No
from Elemento import Elemento
class Lista:
    def __init__(self):
        e = Elemento(None)
        self._cabeca = No(e)
    def getCabeca(self):
        return self._cabeca
    def setCabeca(self, c):
        self._cabeca = c
    def listaVazia(self):
        return self.getCabeca().getProximo() == None
    def mostraLista(self):
        at = self.getCabeca().getProximo()
        while at != None:
            print(at.getElemento().getValor())
            at = at.getProximo()
    def insereNoInicio(self, n):
        n.setProximo(self.getCabeca().getProximo())
        self.getCabeca().setProximo(n)
    def retiraNoInicio(self):
        if not self.listaVazia():
            atual = self.getCabeca().getProximo()
            self._cabeca.setProximo(atual.getProximo())
            atual.setProximo(None)
            return atual
    def insereNoFim(self, n):
        if not self.listaVazia():
            atual = self.getCabeca()
            while atual.getProximo() != None:
                atual = atual.getProximo()
            atual.setProximo(n)
        else:
            self._cabeca.setProximo(n)
    def retiraNoFim(self):
        if not self.listaVazia():
            anterior = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual.getProximo() != None:
                anterior = atual
                atual = atual.getProximo()
            anterior.setProximo(None)
            return atual

    def insereOrdenado(self, v):
        anterior = self.getCabeca()
        atual = self.getCabeca().getProximo()
        while atual != None and atual.getElemento().getValor() < v.getElemento().getValor():
            anterior = atual
            atual = atual.getProximo()
        v.setProximo(atual)
        anterior.setProximo(v)

    def retiraValor(self, x):
        if not self.listaVazia():
            anterior = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual != None and atual.getElemento().getValor() != x:
                anterior = atual
                atual = atual.getProximo()
            if atual != None:
                anterior.setProximo(atual.getProximo())
                atual.setProximo(None)
                return atual
        return None

    def mostraListaRec(self, n):
        if n != None:
            print(n.getElemento().getValor())
            self.mostraListaRec(n.getProximo())

    def mostraListaRecI(self, n):
        if n != None:
            self.mostraListaRecI(n.getProximo())
            print(n.getElemento().getValor())

    def LimpaLista(self, n):
        if n != None:
            self.mostraListaRecI(n.getProximo())
            print(n.getElemento().getValor())
            n.setProximo(None)

    def qtdNosB(self):
        ret = 0
        if not self.listaVazia():
            n = self.getCabeca().getProximo()
            while n:
                n = n.getProximo()
                ret = ret + 1
        return ret
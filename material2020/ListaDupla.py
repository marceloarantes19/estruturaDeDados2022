from NoDupla import NoDupla
from Elemento import Elemento
class Lista:
    def __init__(self):
        e = Elemento(None)
        self._cabeca = NoDupla(e)
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
        segundo = self.getCabeca().getAnterior()
        n.setProximo(segundo)
        self.getCabeca().setAnterior(n)
        if self.getCabeca().getProximo() == None:
            self.getCabeca().setProximo(n)
        else:
            segundo.setAnterior(n)

    def retiraNoInicio(self):
        if not self.listaVazia():
            primeiro = self.getCabeca().getAnterior()
            segundo = primeiro.getProximo()
            self.getCabeca().setAnterior(segundo)
            primeiro.setProximo(None)
            if segundo != None:
                segundo.setAnterior(None)
            else:
                self.getCabeca().setProximo(None)
            return primeiro
        return None

    def insereNoFim(self, n):
        penultimo = self.getCabeca().getProximo()
        n.setAnterior(penultimo)
        self.getCabeca().setProximo(n)
        if self.getCabeca().getAnterior() == None:
            self.getCabeca().setAnterior(n)
        else:
            penultimo.setProximo(n)

    def retiraNoFim(self):
        if not self.listaVazia():
            ultimo = self.getCabeca().getAProximo()
            penultimo = ultimo.getAnterior()
            self.getCabeca().setProximo(penultimo)
            ultimo.setAnterior(None)
            if penultimo != None:
                penultimo.setProximo(None)
            else:
                self.getCabeca().setAnterior(None)
            return ultimo
        return None

    def insereOrdenado(self, v):
        if self.listaVazia():
            self.getCabeca().setAnterior(v)
            self.getCabeca().setProximo(v)
        else:
            ante = self.getCabeca()
            atual = self.getCabeca().getAnterior()
            while atual != None and atual.getElemento().getValor() < v.getElemento().getValor():
                ante = atual
                atual = atual.getProximo()
            if atual == None:
                v.setAnterior(ante)
                ante.setProximo(v)
                self.getCabeca().setProximo(v)
            elif ante == self.getCabeca():
                v.setProximo(atual)
                atual.setAnterior(v)
                self.getCabeca().setAnterior(v)
            else:
                v.setProximo(atual)
                v.setAnterior(ante)
                ante.setProximo(v)
                atual.setAnterior(v)
    def elementoUnico(self):
        p = self.getCabeca().getAnterior()
        u = self.getCabeca().getProximo()
        return not self.listaVazia() and u == p

    def retiraValor(self, x):
        if not self.listaVazia():
            ante = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual != None and atual.getElemento().getValor() != x:
                ante = atual
                atual = atual.getProximo()
            if atual != None:
                if self.elementoUnico():
                    self.getCabeca().setAnterior(None)
                    self.getCabeca().setProximo(None)
                elif self.getCabeca().getAnterior() == atual:
                    trb = atual.getProximo()
                    self.getCabeca().setAnterior(trb)
                    trb.setAnterior(None)
                elif self.getCabeca().getProximo() == atual:
                    trb = atual.getAnterior()
                    self.getCabeca().setProximo(trb)
                    trb.setProximo(None)
                else:
                    trb = atual.getProximo()
                    ante.setProximo(trb)
                    trb.setAnterior(ante)
                atual.setAnterior(None)
                atual.setProximo(None)
                return atual
        return None
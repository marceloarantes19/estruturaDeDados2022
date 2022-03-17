from NoABB import No

class ArvoreBuscaBinaria:
    def __init__(self):
        self._raiz = None
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, n):
        self._raiz = n
    def arvoreVazia(self):
        return self._raiz == None
    def criaNo(self, v):  # ele deve ser inteiro
        no = No()
        no.getElemento().setValor(v)
        return no

    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)

    def insere(self, pai, atual, v):
        if (atual != None):
            if (v < atual.getElemento().getValor()):
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if (v < pai.getElemento().getValor()):
                pai.setFilhoEsquerda(x)
            else:
                pai.setfilhoDireita(x)

    def removeValor(self, v):
        if self.arvoreVazia():
            return None
        else:
            return self.remove(None, self.getRaiz(), v)

    def remove(self, pai, atual, v):
        if atual == None: # Não encontrou o valor
            return None
        elif v < atual.getElemento().getValor(): # procurar na subárvore esquerda
            return self.remove(atual, atual.getFilhoEsquerda(), v)
        elif v > atual.getElemento().getValor(): # procurar na subárvore direita
            return self.remove(atual, atual.getFilhoDireita(), v)
        else: # Encontrou
            # Se é uma folha
            if atual.getFilhoEsquerda() == None and atual.getFilhoDireita() == None:
                if pai == None: # Essa é a raiz da árvore
                    self.setRaiz(None)
                elif atual == pai.getFilhoEsquerda():
                    pai.setFilhoEsquerda(None)
                else:
                    pai.setFilhoDireita(None)
            # Se o nó a apagar possui um único filho à esquerda
            if atual.getFilhoDireita() == None:
                if pai == None:
                    self.setRaiz(atual.getFilhoEsquerda())
                elif atual == pai.getFilhoEsquerda():
                    pai.setFilhoEsquerda(atual.getFilhoEsquerda())
                else:
                    pai.setFilhoDireita(atual.getFilhoEsqurda())
            # Se o nó a apagar possui um único filho à direita
            if atual.getFilhoEsquerda() == None:
                if pai == None:
                    self.setRaiz(atual.getFilhoDireita())
                elif atual == pai.getFilhoEsquerda():
                    pai.setFilhoEsquerda(atual.getFilhoDireita())
                else:
                    pai.setFilhoDireita(atual.getFilhoDireita())
            # se o nó a apagar contém dois filho
            else:
                return self.removeEspecial(atual, atual, atual.getFilhoEsquerda())
            atual.setFilhoEsquerda(None)
            atual.setFilhoDireita(None)
            return atual

    def removeEspecial(self, fixo, pai, atual):
        if atual.getFilhoDireita() != None:
            return self.removeEspecial(fixo, atual, atual.getFilhoDireita())
        else:
            v = fixo.getElemento().getValor()
            fixo.getElemento().setValor(atual.getElemento().getValor())
            atual.getElemento().setValor(v)
            if fixo == pai:
                pai.setFilhoEsquerda(atual.getFilhoEsquerda())
            else:
                pai.setFilhoDireita(atual.getFilhoEsquerda())
            atual.setFilhoEsquerda(None)
            return atual

    def preOrdem(self, no):  # raíz
        if (no != None):
            print(no.getElemento().getValor())
            self.preOrdem(no.getFilhoEsquerda())
            self.preOrdem(no.getFilhoDireita())

    def emOrdem(self, no):  # raíz
        if (no != None):
            self.emOrdem(no.getFilhoEsquerda())
            print(no.getElemento().getValor())
            self.emOrdem(no.getFilhoDireita())

    def posOrdem(self, no):  # raíz
        if (no != None):
            self.emOrdem(no.getFilhoEsquerda())
            self.emOrdem(no.getFilhoDireita())
            print(no.getElemento().getValor())

    def emOrdemInv(self, no):  # raíz
        if (no != None):
            self.emOrdemInv(no.getFilhoDireita())
            print(no.getElemento().getValor())
            self.emOrdemInv(no.getFilhoEsquerda())

    def busca(self, no, v):
        if no == None:
            return False
        elif v == no.getElemento().getValor():
            return True
        elif v < no.getElemento().getValor():
            return self.busca(no.getFilhoEsquerda(), v)
        else:
            return self.busca(no.getFilhoDireita(), v)

    def qtdElementos(self, no):
        if no == None:
            return 0
        else:
            return 1 + self.qtdElementos(no.getFilhoEsquerda()) + self.qtdElementos(no.getFilhoDireita())

    def soma(self, no):
        if no == None:
            return 0
        else:
            at = no.getElemento().getValor()
            es = self.soma(no.getFilhoEsquerda())
            di = self.soma(no.getFilhoDireita())
            return at + es + di

    def menor(self, no):
        if no == None:
            return 99999999
        else:
            at = no.getElemento().getValor()
            es = self.menor(no.getFilhoEsquerda())
            di = self.menor(no.getFilhoDireita())
            me = es if es < di else di
            me = at if at < me else me
            return me

    def maior(self, no):
        if no == None:
            return -99999999
        else:
            at = no.getElemento().getValor()
            es = self.maior(no.getFilhoEsquerda())
            di = self.maior(no.getFilhoDireita())
            ma = es if es > di else di
            ma = at if at > ma else ma
            return ma

    def nivel(self):
        fNo = []
        fNivel = []
        fNo.append(self.getRaiz())
        fNivel.append(0)
        while len(fNo) > 0:
            no = fNo.pop(0)
            nv = fNivel.pop(0)
            print(no.getElemento().getValor(), ' - ', nv)
            if no.getFilhoEsquerda()!=None:
                fNo.append(no.getFilhoEsquerda())
                fNivel.append(nv+1)

            if no.getFilhoDireita()!=None:
                fNo.append(no.getFilhoDireita())
                fNivel.append(nv+1)



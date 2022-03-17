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

    def emOrdemInv(self, no):  # raíz
        if (no != None):
            self.emOrdem(no.getFilhoDireita())
            print(no.getElemento().getValor())
            self.emOrdem(no.getFilhoEsquerda())

    def posOrdem(self, no):  # raíz
        if (no != None):
            self.emOrdem(no.getFilhoEsquerda())
            self.emOrdem(no.getFilhoDireita())
            print(no.getElemento().getValor())

    def busca(self, atual, v):
        if atual == None: # Não encontrou o valor
            return False
        elif v < atual.getElemento().getValor(): # procurar na subárvore esquerda
            return self.busca(atual.getFilhoEsquerda(), v)
        elif v > atual.getElemento().getValor(): # procurar na subárvore direita
            return self.busca(atual.getFilhoDireita(), v)
        else: # Encontrou
            return True

    def qtdE(self, no):
        if no!=None:
            x = self.qtdE(no.getFilhoEsquerda())
            y = self.qtdE(no.getFilhoDireita())
            return x + y + 1
        return 0

    def getSoma(self, no):
        if no!=None:
            x = self.getSoma(no.getFilhoEsquerda())
            y = self.getSoma(no.getFilhoDireita())
            return x + y + no.getElemento().getValor()
        return 0

    def menorDaArvore(self, no):
        if no.getFilhoEsquerda()==None:
            return no.getElemento().getValor()
        else:
            return self.menorDaArvore(no.getFilhoEsquerda())

    def maiorDaArvore(self, no):
        if no.getFilhoDireita()==None:
            return no.getElemento().getValor()
        else:
            return self.maiorDaArvore(no.getFilhoDireita())

    def nivelANivel(self):
        if not self.arvoreVazia():
            f = list()
            f.append(self.getRaiz())
            while len(f) > 0:
                atual = f.pop(0)
                print(atual.getElemento().getValor())
                if atual.getFilhoEsquerda() != None:
                    f.append(atual.getFilhoEsquerda())
                if atual.getFilhoDireita() != None:
                    f.append(atual.getFilhoDireita())

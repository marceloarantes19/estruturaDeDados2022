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

    def removeNo(self, v):
        if self.arvoreVazia():
            return None
        else:
            return self.remove(None, self.getRaiz(), v)

    def remove(self, pai, atual, v):
        if atual == None: # Fim da busca e Não encontrou valor
            return None
        elif v<atual.getElemento().getValor(): # v é menor que o nó, vá para a esquerda
            self.remove(atual, atual.getFilhoEsquerda(), v)
        elif v>atual.getElemento().getValor(): # v é maior que o nó, vá para a direita
            self.remove(atual, atual.getFilhoDireta(), v)
        else: #Encontrou



    def buscaValor(self, pai, valor):
        if pai != None:
            if pai.getElemento().getValor() == valor:
                return True
            else:
                if valor < pai.getElemento().getValor():
                    return self.buscaValor(pai.getFilhoEsquerda(), valor)
                else:
                    return self.buscaValor(pai.getFilhoDireita(), valor)
        return False


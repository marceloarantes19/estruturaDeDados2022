from Elemento import Elemento 
from NoABB import NoABB 
from ArvoreBB import ArvoreBB 

a = ArvoreBB()
l = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]

for i in l:
  e = Elemento(i)
  n = NoABB(e)
  a.insereNo(n)

a.mostraArvore(a.getRaiz(), 0)

# Testa Exercício 1
a.visitaEmOrdemInversa(a.getRaiz())

# Testa Exercício 2
x = a.encontraNoChave(a.getRaiz(), 10)
print(x.getInfo().getChave() if x != None else "Não encontrei")

# Testa Exercício 3
print("Quantidade de Elementos:", a.qtdElem(a.getRaiz()))

# Testa Exercício 4
print("Soma de Elementos:", a.somaElem(a.getRaiz()))

# Testa Exercício 5
print("Menor Elementos:", a.menorElem(a.getRaiz()).getInfo().getChave())

# Testa Exercício 6
print("Maior Elementos:", a.maiorElem(a.getRaiz()).getInfo().getChave())

# Testa Exercício 7
print("Mostra Elementos nível a nível:")

a.mostraNivelANivel()

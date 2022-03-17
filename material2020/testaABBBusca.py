from Elemento import Elemento
from NoABB import No
from ArvoreBuscaBinaria import ArvoreBuscaBinaria

ab = ArvoreBuscaBinaria()
while True:
    valor = int(input('Digite um valor inteiro, ou -1 para sair: '))
    if valor == -1:
        break
    ab.insereNo(valor)
    ab.emOrdem(ab.getRaiz())
valor = int(input('Digite um valor a procurar na árvore , ou -1 para sair: '))
if ab.busca(ab.getRaiz(), valor):
    print("Encontrei o valor!")
else:
    print("Não encontrei o valor!")
print("Quantidade de nós: ", ab.qtdElementos(ab.getRaiz()))
print("Soma: ", ab.soma(ab.getRaiz()))
print("Menor Valor: ", ab.menor(ab.getRaiz()))
print("Maior Valor: ", ab.maior(ab.getRaiz()))
ab.nivel()
#print("A árvore possui: ", ab.qtdE(ab.getRaiz())," nós")
#print("A soma dos valores da árvore é: ", ab.getSoma(ab.getRaiz()))
#print("Árvore Nível a Nível \n\n")
#ab.nivelANivel()

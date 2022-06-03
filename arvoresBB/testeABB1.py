from Elemento import Elemento 
from NoABB import NoABB 
from ArvoreBB import ArvoreBB 

a = ArvoreBB()
ch = int(input("Digite uma chave (-1 para sair): "))
while ch != -1:
  nome = input("Digite um nome: ")
  e = Elemento(ch, nome)
  n = NoABB(e)
  a.insereNo(n)
  print("Árvore Atual")
  a.visitaEmOrdem(a.getRaiz())
  ch = int(input("\n\nDigite uma chave (-1 para sair): "))
print("Pré ordem: ")
a.visitaPreOrdem(a.getRaiz())
print("Pós ordem: ")
a.visitaPosOrdem(a.getRaiz())

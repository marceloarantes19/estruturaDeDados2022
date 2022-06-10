from Elemento import Elemento 
from NoABB import NoABB 
from ArvoreBB import ArvoreBB 

a = ArvoreBB() 
ch = int(input("Digite uma chave (-1 para sair): "))
while ch != -1:
  e = Elemento(ch)
  n = NoABB(e)
  a.insereNo(n)
  print("Árvore Atual")
  a.mostraArvore(a.getRaiz(), 0)
  ch = int(input("\n\nDigite uma chave (-1 para sair): "))

a.mostraArvore(a.getRaiz(), 0)
ch = int(input("\n\nRetirada - Digite uma chave (-1 para sair): "))
while ch != -1 and not a.arvoreVazia():
  n = a.retiraNo(ch)
  if n!=None:
    print("Chave Retirada:", n.getInfo().getChave(),"\n")
  else:
    print("Chave",ch ,"não encontrada!\n")
  if not a.arvoreVazia():
    a.mostraArvore(a.getRaiz(), 0)
    ch = int(input("\n\nRetirada - Digite uma chave (-1 para sair): "))

if a.arvoreVazia():
  print("A árvore está vazia!")
else:
  print("Árvore final: ")
  a.visitaEmOrdemInversa(a.getRaiz())



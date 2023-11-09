from Elemento import Elemento
from No import No
from pilhaEncadeada2023 import PilhaEncadeada
p = PilhaEncadeada()
x = input("Digite um nome: ")
for i in x:
  e = Elemento()
  e.setNome(i)
  n = No(e)
  p.push(n)
x = ""
while not p.pilhaVazia():
  x= x+p.pop().getElemento().getNome()
print(x)
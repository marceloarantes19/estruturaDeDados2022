from Elemento import Elemento
from No import No
from Lista import Lista

lista = Lista()
while True:
    x = int(input('Digite um valor inteiro, ou -1 para sair: '))
    if x == -1:
        break
    e = Elemento(x)
    no = No(e)
    lista.insereOrdenado(no)
    lista.mostraListaRecI(lista.getCabeca().getProximo())



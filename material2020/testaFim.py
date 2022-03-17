from Elemento import Elemento
from No import No
from Lista import Lista

lista = Lista()
while True:
    x = int(input('Digite um valor inteiro, ou -1 para interromper a digitação: '))
    if x == -1:
        break
    e = Elemento(x)
    no = No(e)
    lista.insereNoFim(no)
    lista.mostraLista()
x = int(input('Digite números para retirar o PRIMEIRO elemento da lista ou -1 para sair: '))
while not lista.listaVazia() and x!=-1:
    valor = lista.retiraNoFim()
    print("Valor Retirado: "+str(valor.getElemento().getValor()))
    lista.mostraLista()
    x = int(input('Digite números para retirar o PRIMEIRO elemento da lista ou -1 para sair: '))


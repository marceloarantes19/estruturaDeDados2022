class Pilha:
  def __init__(self):          # Construtor da Classe
    self.__dados = []           # Iniciando a Pilha Vazia

  def pilhaVazia(self):        # Verifica se a pilha está vazia
    return len(self.__dados)==0 # Retorna Verdadeiro se a pilha estiver vazia e falso caso contrário

  def empilha(self, x):        # Insere o elemento valor em x na pilha
    self.__dados.append(x)      # comando para inserir

  def desempilha(self):        # Desempilha um elemento
    x = None
    if not self.pilhaVazia():  # Só pode desempilhar se houver algo na pilha
      x = self.__dados.pop()    # Comando para desempilhar
    return x
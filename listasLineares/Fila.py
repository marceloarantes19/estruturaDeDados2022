class Fila:
  def __init__(self):           # Construtor da Classe
    self.__dados = []           # Iniciando a Fila Vazia

  def filaVazia(self):          # Verifica se a fila está vazia
    return len(self.__dados)==0 # Retorna Verdadeiro se a fila estiver vazia e falso caso contrário

  def enfileira(self, x):       # Insere o elemento valor em x na fila
    self.__dados.append(x)      # comando para inserir

  def desenfileira(self):       # Desenfileira um elemento
    x = None
    if not self.filaVazia():    # Só pode desenfileira se houver algo na fila
      x = self.__dados.pop(0)   # Comando para desenfileira
    return x
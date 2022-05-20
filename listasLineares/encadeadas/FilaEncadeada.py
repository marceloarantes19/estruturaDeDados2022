# Exercício 2 - Correção
from Lista import Lista
class FilaEncadada (Lista):
  def filaVazia(self):
    return self.listaVazia()
  def enQueue(self, n): # Enfileirar
    self.insereNoFim(n)
  def deQueue(self):    # Desenfileirar
    return self.retiraNoInicio()
# Exercício 1 - Correção
from Lista import Lista
class PilhaEncadeada (Lista):
  def pilhaVazia(self):
    return self.listaVazia()
  def push(self, n):    # Empilhar
    self.insereNoInicio(n)
  def pop(self):        # Desempilhar
    return self.retiraNoInicio()
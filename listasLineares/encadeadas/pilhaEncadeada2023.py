from Lista import Lista
class PilhaEncadeada(Lista):
  def pilhaVazia(self):
    return self.listaVazia()
  
  def push(self, n):
    self.insereNoInicio(n)
  
  def pop(self):
    return self.retiraNoInicio()
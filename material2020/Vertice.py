class Vertice:
    def __init__(self):
        self._nome = None
    def getNome(self):
        return self._nome
    def setNome(self, n):
        self._nome = n
    def eVerticePorNome(self, n):
        return self._nome == n

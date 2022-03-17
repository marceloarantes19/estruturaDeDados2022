from Vertice import Vertice
from Aresta import Aresta
from Grafo import Grafo

g = Grafo()
g.adcArestaPorNome("1","2")
g.adcArestaPorNome("1","5")
g.adcArestaPorNome("2","3")
g.adcArestaPorNome("3","4")
g.adcArestaPorNome("5","2")
g.adcArestaPorNome("5","4")
g.adcArestaPorNome("6","4")

g.mostraGrafo()
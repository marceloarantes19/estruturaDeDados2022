class Otima:

	def mergeSort(self, vet, inicio, fim):
		if (fim-inicio) > 1:
			meio = (inicio+fim)//2
			self.mergeSort(vet, inicio, meio)
			self.mergeSort(vet, meio, fim)
			self.intercala(vet, inicio, meio, fim)

	def intercala(self, vet, inicio, meio, fim):
		x = vet[inicio:meio]
		y = vet[meio:fim]
		z = []
		for i in range(0, len(x)+len(y)):
			z.append(0)
		lx = 0
		ly = 0
		lz = 0
		while lz < len(z):
			if lx >= len(x): # x já foi totalmente verificado
			   z[lz] = y[ly]
			   ly = ly + 1
			   lz = lz + 1
			   continue

			if ly >= len(y): # y já foi totalmente verificado
			   z[lz] = x[lx]
			   lx = lx + 1
			   lz = lz + 1
			   continue

			if x[lx] < y[ly]:
				z[lz] = x[lx]
				lx = lx + 1
			else:
				z[lz] = y[ly]
				ly = ly + 1
			lz = lz + 1
		lz = 0
		for i in range(inicio, fim):
			vet[i] = z[lz]
			lz = lz + 1

	def geraHeap(self, arr, n, i):
	    largest = i  # Initialize largest as root
	    l = 2 * i + 1  # left = 2*i + 1
	    r = 2 * i + 2  # right = 2*i + 2
	    # Verifica o filho a esquerda da raiz
	    if l < n and arr[i] < arr[l]:
	        largest = l
	    # Varifica o filho a direita da raiz
	    if r < n and arr[largest] < arr[r]:
	        largest = r
	    # Modifics o raiz, caso seja necessário
	    if largest != i:
	        arr[i], arr[largest] = arr[largest], arr[i]  # swap

	        # Gera o heap com a raiz
	        self.geraHeap(arr, n, largest)

	def heapSort(self, arr):
	    n = len(arr)
	    # Constrói o heap máximo
	    for i in range(n // 2 - 1, -1, -1):
	        self.geraHeap(arr, n, i)
	    # Extraindo cada elemento do Heap e colocando-o na posição correta
	    for i in range(n - 1, 0, -1):
	        arr[i], arr[0] = arr[0], arr[i]  # troca
	        self.geraHeap(arr, i, 0)

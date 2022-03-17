import time
class NaoOtima:

	def bubbleSort(self, x):
		n = len(x)-1
		k = 0
		i = 0
		ini = time.time()
		for i in range(0, n):
			trocou = False
			for j in range(n-1, i-1, -1):
				k = k + 1
				if x[j]>x[j+1]:
					trocou = True
					x[i], x[j] = x[j], x[i]
			if not trocou:
				break
		fim = time.time()
		print("Bubble Sort Total Externo:", i+1)
		print("Bubble Sort Total Interno:", k)
		print("Bubble Sort Tempo:", (fim - ini), "\n")
		return x

	def selectionSort(self, x):
		n = len(x)
		k = 0
		i = 0
		ini = time.time()
		for i in range(0, n-1):
			trocou = False
			for j in range(i+1, n):
				k = k + 1
				if x[i]>x[j]:
					trocou = True
					x[i], x[j] = x[j], x[i]
			if not trocou:
				break
		fim = time.time()
		print("Selection Sort Total Externo:", i+1)
		print("Selection Sort Total Interno:", k)
		print("Selection Sort Tempo:", (fim - ini), "\n")
		return x

	def selectionSort2(self, x):
		n = len(x)
		k = 0
		i = 0
		ini = time.time()
		for i in range(0, n-1):
			trocou = False
			a = i
			for j in range(i+1, n):
				k = k + 1
				if x[a]>x[j]:
					trocou = True
					a = j
			if not trocou:
				break
			x[i], x[a] = x[a], x[i]
		fim = time.time()
		print("Selection Sort alterado Total Externo:", i+1)
		print("Selection Sort alterado Total Interno:", k)
		print("Selection Sort alterado Tempo:", (fim - ini), "\n")
		return x

	def insertionSort(self, x):
		n = len(x)
		k = 0
		i = 0
		ini = time.time()
		for i in range(1, n):
			atual = x[i]
			j = i - 1
			while j >= 0 and atual < x[j]:
				k = k + 1
				x[j+1] = x[j]
				j = j - 1
			x[j+1] = atual
		fim = time.time()
		print("Insertion Sort Total Externo:", i)
		print("Insertion Sort Total Interno:", k)
		print("Insertion Sort Tempo:", (fim - ini), "\n")
		return x

	def shellSort(self, x):
		h = 1
		n = len(x)
		k = 0
		l = 0
		ini = time.time()
		while h < n:
			h = h * 3 + 1
		while h > 1:
			h = h // 3
			for i in range(h, n, h):
				l = l + 1
				atual = x[i]
				j = i - h
				while j >= 0 and atual < x[j]:
					k = k + 1
					x[j+h] = x[j]
					j = j - h
				x[j+h] = atual
		fim = time.time()
		print("Shell Sort Total Externo:", l)
		print("Shell Sort Total Interno:", k)
		print("Shell Sort Tempo:", (fim - ini), "\n")
		return x


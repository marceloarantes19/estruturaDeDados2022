import time
class NaoOtima:

	def bubbleSort(self, x):
		n = len(x)-1
		k = 0
		ini = time.time()
		for i in range(0, n):
			for j in range(n-1, i-1, -1):
				k = k + 1
				if x[j]>x[j+1]:
					x[j], x[j+1] = x[j+1], x[j]
		fim = time.time()
		print("Bubble Externo:", i+1)
		print("Bubble Interno:", k)
		print("Bubble Tempo:", fim-ini, "\n")
		return x

	def selectionSort(self, x):
		n = len(x)
		k = 0
		ini = time.time()
		for i in range(0, n-1):
			for j in range(i+1, n):
				k = k + 1
				if x[i]>x[j]:
					x[i], x[j] = x[j], x[i]
		fim = time.time()
		print("Selection Externo:", i+1)
		print("Selection Interno:", k)
		print("Selection Tempo:", fim-ini, "\n")
		return x

	def insertionSort(self, x):
		n = len(x)
		k = 0
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
		print("Insertion Externo:", i)
		print("Insertion Interno:", k)
		print("Insertion Tempo:", fim-ini, "\n")
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
				atual = x[i]
				j = i - h
				l = l + 1
				while j >= 0 and atual < x[j]:
					k = k + 1
					x[j+h] = x[j]
					j = j - h
				x[j+h] = atual
		fim = time.time()
		print("Shell Externo:", l)
		print("Shell Interno:", k)
		print("Shell Tempo:", fim-ini, "\n")
		return x


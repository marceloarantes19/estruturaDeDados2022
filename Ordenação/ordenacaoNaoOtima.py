class NaoOtima:

	def bubbleSort(self, x):
		n = len(x)-1
		for i in range(0, n):
			for j in range(n-1, i-1, -1):
				if x[j]>x[j+1]:
					t = x[j]
					x[j] = x[j+1]
					x[j+1] = t
		return x

	def selectionSort(self, x):
		n = len(x)
		for i in range(0, n-1):
			for j in range(i+1, n):
				if x[i]>x[j]:
					x[i], x[j] = x[j], x[i]
		return x

	def insertionSort(self, x):
		n = len(x)
		for i in range(1, n):
			atual = x[i]
			j = i - 1
			while j >= 0 and atual < x[j]:
				x[j+1] = x[j]
				j = j - 1
			x[j+1] = atual
		return x

	def shellSort(self, x):
		h = 1
		n = len(x)
		while h < n:
			h = h * 3 + 1
		while h > 1:
			h = h // 3
			for i in range(h, n, h):
				atual = x[i]
				j = i - h
				while j >= 0 and atual < x[j]:
					x[j+h] = x[j]
					j = j - h
				x[j+h] = atual
		return x


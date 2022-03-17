class BubbleSort:
	def bubble(self, x):
		n = len(x)-1
		for i in range(0, n):
			for j in range(n-1, i-1, -1):
				if x[j]>x[j+1]:
					t = x[j]
					x[j] = x[j+1]
					x[j+1] = t
		return x

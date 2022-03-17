from ordenacaoNaoOtimaCA import NaoOtima
import random
obj = NaoOtima()
n = 1000
a = []
for i in range(0, n):
	a.append(n-i)
a = obj.bubbleSort(a)

a = []
for i in range(0, n):
	a.append(n-i)
a = obj.selectionSort(a)

a = []
for i in range(0, n):
	a.append(n-i)
a = obj.insertionSort(a)

a = []
for i in range(0, n):
	a.append(n-i)
a = obj.shellSort(a)

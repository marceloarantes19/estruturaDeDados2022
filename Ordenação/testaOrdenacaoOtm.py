from ordenacaoOtima import Otima
obj = Otima()
n = 20
a = []
for i in range(0, n):
	a.append(n-i)
obj.mergeSort(a, 0, len(a))
#obj.heapSort(a)
print(a)


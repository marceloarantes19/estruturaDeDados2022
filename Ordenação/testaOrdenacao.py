from ordenacaoNaoOtima import NaoOtima
obj = NaoOtima()
n = 10
a = []
for i in range(0, n):
	a.append(n-i)
print(a)
a = obj.bubbleSort(a)

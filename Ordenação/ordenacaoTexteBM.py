import time
def insertionSort(x):
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
	#print("Insertion Externo:", i)
	print("Insertion Interno:", k)
	print("\n\n**********   Insertion Tempo:", fim-ini, "\n\n")
	return x

a = []
for i in range(10000,0,-1):
	a.append(i)
#print(a)
a = insertionSort(a)
#print(a)
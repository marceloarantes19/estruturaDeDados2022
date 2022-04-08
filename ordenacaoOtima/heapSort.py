def geraHeap(arr, n, i):
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
        geraHeap(arr, n, largest)

def heap(arr):
    n = len(arr)
    # Constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        geraHeap(arr, n, i)
    # Extraindo cada elemento do Heap e colocando-o na posição correta
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # troca
        geraHeap(arr, i, 0)


x = [2, 7, 8, 1, 3, 6, 9]
heap(x)
print("Fim do algoritmo -", x)
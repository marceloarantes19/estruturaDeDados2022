def fat(n):
    return 1 if n == 0 else n * fat(n-1)

def mdc(x, y):
    return x if y == 0 else mdc(y, x % y)

x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))

print(mdc(x,y))
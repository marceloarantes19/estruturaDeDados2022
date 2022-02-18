x = int(input('Digite um número entre 100 e 999: '))
u = x % 10
x = x // 10
d = x % 10
c = x // 10
print('Unidade: ', u)
print('Dezena.: ', d)
print('Centena: ', c)

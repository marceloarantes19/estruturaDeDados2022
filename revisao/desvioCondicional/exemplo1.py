A = float(input('Digite o primeiro valor: '))
B = float(input('Digite o segundo valor.: '))
soma = A + B
prod = A * B
dife = A - B
print(f'Soma.....: {soma:.2f}')
print(f'Produto..: {prod:.2f}')
print(f'Diferença: {dife:.2f}')
if B != 0:
  quoc = A / B
  print(f'Quociente: {quoc:.2f}')
else:
  print('Não Existe divisão por zero.')
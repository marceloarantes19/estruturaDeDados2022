x1 = float(input('Informe o x do primeiro ponto: '))
y1 = float(input('Informe o y do primeiro ponto: '))
x2 = float(input('Informe o x do segundo ponto.: '))
y2 = float(input('Informe o y do segundo ponto.: '))
h = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f'A distância entre os dois pontos é: {h:.2f}')

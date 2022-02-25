a = float(input('Digite o primeiro coeficiente: '))
b = float(input('Digite o segundo coeficiente.: '))
c = float(input('Digite o terceiro coeficiente: '))
if a == 0:
  print('Não é uma equação do segundo grau!')
else:
  delta = b ** 2 - 4 * a * c
  print('Delta', delta)
  if delta < 0:
    print('Equação não possui raizes.')
  else:
    x = (-b + delta ** 0.5)/(2*a)
    print(f"{x:.2f} é uma raiz para a equação")
    if delta>0:
      x = (-b - delta ** 0.5)/(2*a)
      print(f"{x:.2f} é outra raiz para a equação")


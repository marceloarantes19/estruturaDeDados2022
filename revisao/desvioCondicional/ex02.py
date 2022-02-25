# Dados Peso e altura, determine a quantidade de quilos a ganhar ou 
# a perder para que se atinja o peso ideal
peso = float(input("Digite o Peso (em Kg).: "))
altura = float(input("Digite a altura (em m): "))
imc = peso / (altura ** 2)
print(f'O IMC é: {imc:.2f}')
if imc < 18.5:
  print('Abaixo do Peso')
elif imc < 25:
  print('Peso normal')
elif imc < 30:
  print('Sobrepeso')
elif imc<40:
  print('Obeso Moderado')
else:
  print('Obeso Mórbido')

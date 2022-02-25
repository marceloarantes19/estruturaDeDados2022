# Dados Peso e altura, determine a quantidade de quilos a ganhar ou 
# a perder para que se atinja o peso ideal
peso = float(input("Digite o Peso (em Kg).: "))
altura = float(input("Digite a altura (em m): "))
imc = peso / (altura ** 2)
print(f'O IMC é: {imc:.2f}')
if imc < 18.5:
	ideal = 18.5 * (altura ** 2)
	precisa = ideal - peso
	print(f"Está abaixo do peso e precisa ganhar ao menos {precisa:.2f} Kg.")
elif imc < 25:
  print('Peso normal')
else:
	ideal = 25 * (altura ** 2)
	precisa = peso - ideal
	print(f"Está acima do peso e precisa perder ao menos {precisa:.2f} Kg.")
	
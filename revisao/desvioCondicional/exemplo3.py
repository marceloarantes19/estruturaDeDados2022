n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a segunda Nota.: '))
media = (n1+n2)/2
print(f'Média: {media:.1f}')
if media < 0 or media > 10:
  print('Existem notas fora do intervalo - 0 a 10')
elif media<3:
  print('Retido!')
elif media<7:
  print('Final!')
elif media<9.6:
  print('Aprovado!')
else:
  print('Aprovado com Louvor!')

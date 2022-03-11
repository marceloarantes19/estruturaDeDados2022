x = input("Digite uma palavra: ")
y = True
for i in range(0, len(x)//2):
  if x[i] != x[len(x)-i-1]:
    y = False
    break

if y:
  print(x," é palindrome!")
else:
  print(x, " não é palindrome!") 


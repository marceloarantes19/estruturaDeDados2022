x = input("Digite uma palavra: ")
y = ""
for i in x:
  y = i + y

if x == y:
  print(x," é palindrome!")
else:
  print(x, " não é palindrome!")


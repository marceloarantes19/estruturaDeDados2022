def merge(vet, inicio, fim):
  if (fim-inicio) > 1:
    meio = (inicio+fim)//2
    merge(vet, inicio, meio)
    merge(vet, meio, fim)
    intercala(vet, inicio, meio, fim)

def intercala(vet, inicio, meio, fim):
  x = vet[inicio:meio]
  y = vet[meio:fim]
  z = []
  for i in range(0, len(x)+len(y)):
    z.append(0)
  lx = 0
  ly = 0
  lz = 0
  while lz < len(z):
    if lx >= len(x): # x já foi totalmente verificado
        z[lz] = y[ly]
        ly = ly + 1
        lz = lz + 1
        continue

    if ly >= len(y): # y já foi totalmente verificado
        z[lz] = x[lx]
        lx = lx + 1
        lz = lz + 1
        continue

    if x[lx] < y[ly]:
      z[lz] = x[lx]
      lx = lx + 1
    else:
      z[lz] = y[ly]
      ly = ly + 1
    lz = lz + 1
  lz = 0
  for i in range(inicio, fim):
    vet[i] = z[lz]
    lz = lz + 1

x = [2, 7, 8, 1, 3, 6]
merge(x,0,len(x))
print("Fim do algoritmo -", x)
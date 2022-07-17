vet = []
j = int(input("Digite o tamanho do vetor: "))
i = 0;
for i in range(j):
  vet.append(int(input(f'Digite o {i+1}º valor: ')))
vet2 = []
def outrovetor(vet, tam):
  ret = []
  i = 0;
  for i in range(tam//2):
    ret.append(vet[(tam//2)+i])
  return ret;

vet2 = outrovetor(vet, j);

print(vet2)

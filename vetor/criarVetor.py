vetor = [];
i = 0;
j = 0;
v = int(input("Digite o tamanho do vetor: "));
aux = [];
lastvet = [];
for i in range(v):
  vetor.append([0]*v)
for i in range(v):
  aux.append([0]*v)
for i in range(v):
  lastvet.append([0]*v)
print("Digite os valores do primeiro Vetor: ")
for i in range(v):
  for j in range(v):
    vetor[i][j] = int(input(f'Digite um valor para a coluna {i+1} linha {j+1}: '))
print("Digite os valores do segundo Vetor: ")
for i in range(v):
  for j in range(v):
    aux[i][j] = int(input(f'Digite um valor para a coluna {i+1} linha {j+1}: '))

for i in range(v):
  for j in range(v):
    if aux[i][j] > vetor[i][j]:
      lastvet[i][j] = aux[i][j];
    else:
      lastvet[i][j] = vetor[i][j];

for i in range(v):
  for j in range(v):
    print(lastvet[i][j]," ", end=" ")
  print()


import random

lista = []
acima = []
abaixo = []
soma = 0

for n in range(20):
  lista.append(random.randint(0, 100))

for i in range(len(lista)):
  soma = soma + lista[i]

media = soma / int(len(lista))

for i in range(len(lista)):
  if lista[i] > media:
    acima.append(lista[i])
  else:
    abaixo.append(lista[i])

print("Média:", media)
print("Valores acima da média:", acima)
print("Valores abaixo da média:",abaixo)
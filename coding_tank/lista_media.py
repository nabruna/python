import random

lista = []
soma = 0

for n in range(20):
  lista.append(random.randint(0, 100))

for i in range(len(lista)):
  soma += lista[i]

media = soma / int(len(lista))
print("Média:", media)
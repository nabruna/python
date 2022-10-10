import random

lista = []

for n in range(20):
  lista.append(random.randint(0, 100))

for i in range(len(lista)):
  if lista[i] % 2 == 0:
    print(lista[i])
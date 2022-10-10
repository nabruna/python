import random

prompt = "Digite quantas atividades foram realizadas: " 
atividades = int(input(prompt))
notas = []
soma = 0

for n in range(atividades):
  notas.append(random.randint(0, 100))

menor = min(notas)
maior = max(notas)

print(notas)

print("Menor nota:", menor)
print("Maior nota:", maior)

notas.remove(menor)
notas.remove(maior)

for x in range(len(notas)):
  soma = soma + notas[x]

media = soma / (atividades - 2)

print("Média:", media)
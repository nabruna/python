vetor1 = []
vetor2 = []

for n in range(3):
  coord = int(input("Digite uma coordenada para o primeiro vetor: "))
  vetor1.append(coord)

for n in range(3):
  coord = int(input("Digite uma coordenada para o segundo vetor: "))
  vetor2.append(coord)

for coord in vetor1:
  for coord in vetor2:
    soma1 = vetor1[0] + vetor2[0]
    soma2 = vetor1[1] + vetor2[1]
    soma3 = vetor1[2] + vetor2[2]

print(f"A soma dos valores {vetor1[0]} + {vetor2[0]} = {soma1}")
print(f"A soma dos valores {vetor1[1]} + {vetor2[1]} = {soma2}")
print(f"A soma dos valores {vetor1[2]} + {vetor2[2]} = {soma3}")
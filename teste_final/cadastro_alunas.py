prompt = "Digite a quantidade de alunas a serem cadastradas: " 
alunas = int(input(prompt))
notas = []
soma_notas = 0
soma_vari = 0

for aluna in range(alunas):
  nota = float(input(f"Digite a nota da {aluna+1}a aluna: "))
  notas.append(nota)

for nota in notas:
  soma_notas += nota

media = soma_notas / alunas

for nota in notas:
  soma_vari += ((nota - media) ** 2)

variancia = soma_vari / (alunas - 1)

print(f"As alunas possuem as seguintes notas: {notas} com média de {'{:.2f}'.format(media)} e variância de {'{:.2f}'.format(variancia)}")

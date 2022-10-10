prompt = "Digite o nome da aluna: " 
nome = input(prompt)

prompt = "Digite sua matrícula: " 
matricula = int(input(prompt))

prompt = "Digite a quantidade de provas realizadas: " 
qtde_provas = int(input(prompt))

notas = []
for prova in range(qtde_provas):
  nota = float(input(f"Digite a nota da {prova+1}a prova: "))
  notas.append(nota)

prompt = "Digite o percentual de presencas da aluna: " 
presenca = float(input(prompt))

soma_notas = 0
status = False

for nota in notas:
  soma_notas += nota
media = soma_notas / qtde_provas

if presenca >= 70 and media >= 6.0:
  status = True

aluna = []
aluna.append(matricula)
aluna.append(nome)
aluna.append(notas)
aluna.append(media)
aluna.append(presenca)
aluna.append(status)

print(aluna)
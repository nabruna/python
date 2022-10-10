notas_totais = 0
provas = 0
nota = 0

while nota >= 0: 
  prompt = "Digite uma nota: "
  nota = float(input(prompt))
  notas_totais += nota
  provas += 1

media = (notas_totais - nota) / (provas - 1)
print("Média:", media)
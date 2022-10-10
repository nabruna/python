prompt = "Digite quantas provas foram realizadas: " 
provas = int(input(prompt))
notas_totais = 0

for prova in range (provas):
  nota = float(input(f"Digite a nota da prova {prova + 1}: "))
  notas_totais += nota

media = notas_totais / provas
print("Média:", media)
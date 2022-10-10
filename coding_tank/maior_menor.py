prompt = "Digite quantas provas foram realizadas: " 
provas = int(input(prompt))
notas_totais = 0
nota_maior = 0
nota_menor = 1000

for prova in range (provas):
  nota = float(input(f"Digite a nota da prova {prova + 1}: "))
  if nota > nota_maior:
    nota_maior = nota
  elif nota < nota_menor:
    nota_menor = nota 
  notas_totais += nota

media = notas_totais / provas
print("Média:", media)
print("Maior nota:", nota_maior)
print("Menor nota:", nota_menor)
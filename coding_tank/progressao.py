prompt = "Digite a razão da progressão aritimética: " 
razao = int(input(prompt))

prompt = "Digite o termo inicial da progressão aritimética: " 
termo_inicial = int(input(prompt))

prompt = "Digite quantos termos gostaria de ver na tela: " 
qtde_termos = int(input(prompt))

for termo in range (qtde_termos):
  print(termo_inicial)
  termo_inicial += razao
produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]
encontrado = False
resp = ""

while resp != "sair":
  prompt = "Digite o nome do produto: " 
  nome_produto = input(prompt)

  for produto, preco in produtos:  
    if produto == nome_produto:
      print(f"{produto}: R${preco}")
      encontrado = True
      break

  if encontrado == False:
    print("Produto não encontrado.")

  prompt = 'Digite "sair" para sair: '
  resp = input(prompt)
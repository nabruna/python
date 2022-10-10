prompt = "Digite quanto dinheiro deseja aplicar: " 
montante = float(input(prompt))

prompt = "Selecione o fundo desejado: (A, B, C, D, E) " 
fundo = input(prompt)

prompt = "Digite a quantidade de anos para a aplicação: " 
tempo_aplicacao = int(input(prompt))

if fundo == "A" or fundo == "a":
  if montante < 50:
    print("Valor inicial insuficiente.")
  else:
    rendimento = montante * ((1 + 0.1) ** tempo_aplicacao)
    print("Rendimento total:", rendimento)
elif fundo == "B" or fundo == "b":
  if montante < 100:
    print("Valor inicial insuficiente.")
  elif tempo_aplicacao < 1:
    print("Tempo de aplicação insuficiente.")
  else:
    rendimento = montante * ((1 + 0.12) ** tempo_aplicacao)
    print("Rendimento total:", rendimento)
elif fundo == "C" or fundo == "c":
  if montante < 500:
    print("Valor inicial insuficiente.")
  elif tempo_aplicacao < 2:
    print("Tempo de aplicação insuficiente.")
  else:
    rendimento = montante * ((1 + 0.13) ** tempo_aplicacao)
    print("Rendimento total:", rendimento)
elif fundo == "D" or fundo == "d":
  if montante < 1000:
    print("Valor inicial insuficiente.")
  elif tempo_aplicacao < 3:
    print("Tempo de aplicação insuficiente.")
  else:
    rendimento = montante * ((1 + 0.15) ** tempo_aplicacao)
    print("Rendimento total:", rendimento)
elif fundo == "E" or fundo == "e":
  if montante < 3000:
    print("Valor inicial insuficiente.")
  elif tempo_aplicacao < 5:
    print("Tempo de aplicação insuficiente.")
  else:
    rendimento = montante * ((1 + 0.18) ** tempo_aplicacao)
    print("Rendimento total:", rendimento)
else:
  print("Não é possível realizar essa aplicação.")
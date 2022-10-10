prompt = "Digite o ano: " 
ano_bi = int(input(prompt))

if ano_bi % 4 == 0:
  if ano_bi % 100 == 0 and ano_bi % 400 == 0:
    print("É bissexto.")
  elif ano_bi % 100 == 0:
    print("Não é bissexto.")
  else:
    print("É bissexto.")
else:
  print("Não é bissexto.")
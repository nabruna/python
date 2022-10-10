prompt = "Digite um número para descobrir sua tabuada: " 
tabuada = int(input(prompt))
contador = 1

for x in range (10):
  print(tabuada, "x", contador, "=", tabuada * contador)
  contador += 1
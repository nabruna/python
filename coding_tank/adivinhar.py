import random
repetir = "Sim"

while repetir == "Sim" or repetir == "sim":
  num_sorteado = random.randint(1, 100)
  num_chute = 0

  while num_sorteado != num_chute:
    prompt = "Digite um número de 1 a 100: " 
    num_chute = int(input(prompt))
    
    if num_sorteado == num_chute:
      print("Acertou! O número sorteado foi", num_chute)
      break
    else:
      print("Errou! Tente novamente.")
    
  prompt = "Deseja jogar novamente: " 
  repetir = input(prompt)

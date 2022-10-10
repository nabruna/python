import random

resp = "S"
resultado = ""
jogada = 1000

prompt = "Digite Pedra, Tesoura ou Papel para jogar: "
escolha = input(prompt)
sorteio = random.randint(0, 2)

if escolha == "Pedra":
  jogada = 0
elif escolha == "Tesoura":
  jogada = 1
elif escolha == "Papel":
  jogada == 2
else:
  resultado = ("Escolha inválida.")

if jogada == sorteio:
  resultado = "Empate..."
elif (jogada == 0 and sorteio == 1) or (jogada == 1 and sorteio == 2) or (jogada == 2 and sorteio == 0):
  resultado = "Você venceu!"
else:
  resultado = "Você perdeu."

print(sorteio)
print(escolha)
print(resultado)
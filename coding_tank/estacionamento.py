prompt = "Digite quanto tempo em horas o carro ficou estacionado: " 
tempo = int(input(prompt))

valor_total = 5 * (tempo - 1) + 10

print("O valor do estacionamento ficou em", valor_total)
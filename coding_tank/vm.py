prompt = "Digite a distância total da sua viagem em km: " 
distancia = int(input(prompt))

prompt = "Digite o quanto tempo demorou sua viagem em horas: " 
tempo = int(input(prompt))

velocidade = distancia / tempo

print("A sua velocidade média foi de", velocidade, "km/h")
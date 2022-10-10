prompt = "Digite qual será o capital inicial: " 
capital = float(input(prompt))

prompt = "Digite a taxa de juros ao mês em porcentagem: " 
taxa = float(input(prompt))

prompt = "Digite a quantidade de meses de duração da aplicação: " 
tempo = int(input(prompt))

rendimento = capital * ((1 + (taxa / 100)) ** tempo)

percent = (rendimento * 100) / capital

print("O rendimento do investimento será de", rendimento)
print("O valor recebido apenas em juros foi de", rendimento - capital)
print("A aplicação rendeu um total de", int(percent), "%")
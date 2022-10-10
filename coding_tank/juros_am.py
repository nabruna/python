prompt = "Digite quanto dinheiro deseja aplicar: " 
montante = float(input(prompt))

prompt = "Informe a taxa de juros ao mês (em %): " 
taxa_juros = float(input(prompt))

prompt = "Digite a quantidade de meses de duração da aplicação: " 
tempo_aplicacao = int(input(prompt))

contador = 0

while contador != tempo_aplicacao:
  juros_totais = montante * (taxa_juros / 100)
  faturamento = montante + juros_totais
  montante = faturamento
  print(f"Mês {contador + 1}: Juros: {format(juros_totais, '.2f')} reais, saldo: {format(faturamento, '.2f')} reais")
  contador += 1

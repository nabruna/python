tabela_price = []

prompt = "Digite o valor do empréstimo: " 
emprestimo = float(input(prompt))

prompt = "Digite a taxa de juros em porcentagem: " 
juros = float(input(prompt))

prompt = "Digite a quantidade de meses para pagamento: " 
tempo = int(input(prompt))
valor_inicial = emprestimo
valor_pago = emprestimo
amortizacao = 0
taxa = juros / 100
pgto = emprestimo * ((((1 + taxa) ** tempo) * taxa) / (((1 + taxa) ** tempo) - 1))

for i in range(tempo):
  juros_aplicados = taxa * valor_inicial
  valor_pago = valor_inicial + juros_aplicados - pgto
  amortizacao = pgto - juros_aplicados
  valor_inicial = valor_pago

  tabela_price.append([i+1, '{:.2f}'.format(juros_aplicados), '{:.2f}'.format(amortizacao), '{:.2f}'.format(pgto), '{:.2f}'.format(valor_inicial)])
mes = 1

while mes >= 1:
  prompt = "Qual mês deseja consultar? " 
  mes = int(input(prompt))

  for x in tabela_price:
    if mes == x[0]:
      print(f"Mês: {x[0]} \t Juros: {x[1]} \t Amortização: {x[2]} \t Saldo devedor: {x[4]}")

  if mes > tempo or mes <= 0:
    print("Mês não existe.")
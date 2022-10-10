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
  print(f"Parcela {i+1} \t Juros: R${'{:.2f}'.format(juros_aplicados)} \t Amortização: {'{:.2f}'.format(amortizacao)} \t Pagamento: {'{:.2f}'.format(pgto)} \t Saldo devedor: {'{:.2f}'.format(valor_inicial)}")
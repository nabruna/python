prompt = "Digite o salário atual: " 
salario = float(input(prompt))

prompt = "Digite a porcentagem de aumento sobre o salário: " 
aumento = int(input(prompt))

novo_salario = salario + (salario * (aumento / 100))

print("O novo salário da funcionária é de", novo_salario)
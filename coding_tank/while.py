prompt = "Digite um número inteiro positivo: " 
num_while = int(input(prompt))

prompt = "Digite outro número inteiro positivo: " 
num2_while = int(input(prompt))

prompt = "Digite o passo da contagem: " 
passo = int(input(prompt))

if num_while >= num2_while:
  while num_while >= num2_while:
    print(num2_while)
    num2_while += passo
elif num_while < num2_while:
  while num_while <= num2_while:
    print(num_while)
    num_while += passo

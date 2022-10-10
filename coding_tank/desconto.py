prompt = "Digite o preço do produto: " 
preco = float(input(prompt))

prompt = "Digite a porcentagem de desconto a ser aplicado: " 
desconto = int(input(prompt))

preco_final = preco - (preco * (desconto / 100))

print("O valor final a ser pago é de", preco_final)
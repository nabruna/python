prompt = "Digite uma base: " 
base = int(input(prompt))

prompt = "Digite um expoente: " 
expoente = int(input(prompt))
nova_base = base

if expoente > 1:
  for i in range(expoente - 1):
    resultado = nova_base * base
    nova_base = resultado
elif expoente == 1:
  resultado = base
elif expoente < 1:
  resultado = 1

print(resultado)
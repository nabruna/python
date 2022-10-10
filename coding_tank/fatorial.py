prompt = "Digite um número inteiro positivo: " 
num = int(input(prompt))
fatorial = 1

if num <= 0:
  print("Número precisa ser positivo.")
else:
  while num > 1:
    fatorial *= num
    num -= 1
  print("Fatorial:", fatorial)
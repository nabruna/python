prompt = "Digite um número inteiro positivo: " 
num = int(input(prompt))
fatorial = 1

if num <= 0:
  print("Número precisa ser positivo.")
else:
  for x in range (num):
    fatorial *= num
    num -= 1
  print("Fatorial:", fatorial)
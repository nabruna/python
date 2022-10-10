prompt = "Digite um número inteiro positivo: " 
num = int(input(prompt))
soma = 0

if num <= 0:
  print("Número precisa ser positivo.")
else:
  for x in range (num):
    soma += num
    num -= 1
  print("Soma total:", soma)
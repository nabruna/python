prompt = "Digite um número: " 
num = float(input(prompt))

if num == 0:
  print("Este número é zero.")
elif num % 2 == 0:
  print("Este número é par.")  
else:
  print("Este número é ímpar.")
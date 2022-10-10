prompt = "Digite um número: " 
num = float(input(prompt))

if num > 0:
  print("Este número é positivo.")
elif num < 0:
  print("Este número é negativo.")
else:
  print("Este número é zero.")
prompt = "Digite o coeficiente a: " 
a = float(input(prompt))

prompt = "Digite o coeficiente b: " 
b = float(input(prompt))

prompt = "Digite o coeficiente c: " 
c = float(input(prompt))

delta = (b ** 2) - (4 * a * c)

if delta == 0:
  raiz = (- b) / (2 * a)
  print("A equação possui raiz ", raiz)
elif delta < 0:
  print("A equação não possui raízes reais.")
else:
  raiz1 = (- b + (delta ** 0.5)) / (2 * a)
  raiz2 = (- b - (delta ** 0.5)) / (2 * a)
  print("A equação possui as raízes", raiz1, raiz2)
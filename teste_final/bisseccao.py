prompt = "Digite um número positivo para cálculo da raiz quadrada: " 
x = float(input(prompt))

prompt = "Digite o valor de precisão: " 
e = float(input(prompt))

i = 0
f = x

while f - i > e:
  m = i + ((f - i) / 2)
  if m ** 2 > x:
    f = m
  else:
    i = m

print("Número escolhido:", x)
print("Raiz aproximada:", m)
prompt = "Digite quantos com quantos termos deseja calcular pi: " 
termos_pi = int(input(prompt))

n1 = 0
n2 = 0
for i in range(termos_pi):
  if i % 2 != 0:
    n2 += 1
    if n2 % 2 == 0:
      n1 -= 1 / i
    else:
      n1 += 1 / i
print(n1 * 4)
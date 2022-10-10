prompt = "Digite o tamanho do primeiro lado: " 
l1 = int(input(prompt))

prompt = "Digite o tamanho do segundo lado: " 
l2 = int(input(prompt))

prompt = "Digite o tamanho do terceiro lado: " 
l3 = int(input(prompt))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
  print("Triângulo não existe.")
else:
  print("Triângulo existe.")
  if l1 == l2 and l2 == l3 and l1 == l3:
    print("Tipo do triângulo: equilátero.")
  elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Tipo do triângulo: isósceles.")
  elif l1 != l2 and l2 != l3 and l1 != l3:
    print("Tipo do triângulo: escaleno.")
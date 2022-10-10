prompt = "Digite a primeira nota: " 
n1 = float(input(prompt))

prompt = "Digite a segunda nota: " 
n2 = float(input(prompt))

media = (n1 + n2) / 2

if media >= 70:
  print("Aprovada com média", media)
elif media >= 30 and media < 70:
  print("Em exame com média", media)

  prompt = "Digite a nota do exame: " 
  exame = float(input(prompt))

  media_exame = (media + exame) / 2

  if media_exame > 50:
    print("Aprovada por exame com média", media_exame)
  else:
    print("Reprovada com média", media_exame)
elif media < 30:
  print("Reprovada com média", media)
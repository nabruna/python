prompt = "Qual o seu nome? " 
nome_usuaria = input(prompt)

prompt = "Qual é seu gênero? (M, F, Neutro ou Outro) " 
genero = input(prompt)

if genero == "M" or genero == "m":
  print("Seja bem-vindo", nome_usuaria)
elif genero == "F" or genero == "f":
  print("Seja bem-vinda", nome_usuaria)
elif genero == "Neutro" or genero == "Outro" or genero == "neutro" or genero == "outro":
  print("Seja bem-vind@", nome_usuaria)
else:
  print("Opção inválida.")
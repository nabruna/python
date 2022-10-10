prompt = "Qual o seu nome? " 
nome_usuaria = input(prompt)
genero = ""

while genero != 'M' or genero != 'F' or genero != 'Neutro' or genero != 'Outro':
  prompt = "Qual é seu gênero? (M, F, Neutro ou Outro) " 
  genero = input(prompt)  
  if genero == 'M':
    print("Seja bem-vindo", nome_usuaria)
    break
  elif genero == 'F':
    print("Seja bem-vinda", nome_usuaria)
    break
  elif genero == 'Neutro' or genero == 'Outro':
    print("Seja bem-vind@", nome_usuaria)
    break
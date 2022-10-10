idade = input("Idade: ")
peso = input("Peso: ")
altura = input("Altura: ")
aptitude = False

if int(idade) > 18 and int(peso) >= 60 and float(altura) >= 1.6:
    aptitude = True

if aptitude == True:
    print("Pessoa é apta a entrar no exército.")
else:
    print("Pessoa não é apta a entrar no exército.")
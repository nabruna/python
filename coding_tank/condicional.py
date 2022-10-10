prompt = "Qual o seu nome? " 
nome_usuaria = input(prompt)

prompt = "Que horas são? " 
horario = int(input(prompt))

if horario < 0:
  print("Horário inválido.")
elif horario >= 4 and horario <= 11:
  print("Bom dia", nome_usuaria)
elif horario >= 12 and horario <= 17:
  print("Boa tarde", nome_usuaria)
elif horario >= 18 and horario <= 23:
  print("Boa noite", nome_usuaria)
elif horario > 23:
  print("Horário inválido.")
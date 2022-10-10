prompt = "Digite o número inicial: " 
inicio = int(input(prompt))

prompt = "Digite o número final: " 
fim = int(input(prompt))

lista = []
contador = 0

if fim > inicio:
  qtde = fim - inicio
  for x in range(qtde): 
    lista.append(inicio + contador)
    contador += 1
else:
  qtde = inicio - fim 
  for x in range(qtde): 
    lista.append(inicio - contador)
    contador += 1

lista.append(fim)
print(lista)
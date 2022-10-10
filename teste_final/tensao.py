prompt = "Digite o valor da tensão da fonte de alimentação: " 
tensao = float(input(prompt))

prompt = "Digite a tensão do primeiro resistor em paralelo: " 
r1 = float(input(prompt))

prompt = "Digite a tensão do segundo resistor em paralelo: " 
r2 = float(input(prompt))

resistor_equivalente = (r1 * r2) / (r1 + r2)
corrente = tensao / resistor_equivalente

print(f"O resistor equivalente deve possuir tensão de {resistor_equivalente} e a corrente será de {corrente}.")
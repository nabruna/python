prompt = "Digite o valor da temperatura em Fahrenheit: " 
fahrenheit = float(input(prompt))

celsius = ((fahrenheit - 32) * 5) / 9

print("Esta temperatura corresponde a", celsius, "°C")
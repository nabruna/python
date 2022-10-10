prompt = "Digite quantos valores da sequência de Fibonacci gostaria de ver na tela: " 
qtde_fibo = int(input(prompt))
fibo = 1
fibo1 = 1
fibo2 = 1

for fibo in range(qtde_fibo):
    print(fibo1)
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo
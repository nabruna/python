"""
Exercício:

1. Crie uma lista de compras com 5 elementos
2. Transforme a lista em tupla
3. Imprima os 3 elementos centrais utilizando slice
4. Itere sobre os itens da tupla e imprima: o nome do item e quantas letras ele possui
"""

lista_de_compras = ["Papel higiênico", "Pão", "Açúcar", "Chá", "Desinfetante"]

tuple(lista_de_compras)

print(lista_de_compras[1:4])

for item in lista_de_compras:
    print(f"{item}: {len(item)} \n")
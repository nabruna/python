"""
### Tupla (tuple) ###

definição: é um container que armazena elementos/objetos
de forma sequencial, imutável e iterável.
"""

# criando uma tupla
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
tupla2 = (1, 2, 3, [1, 2, 3])

# verificando o tipo
type(tupla)


# criando uma tupla mista
mista = (1, 2, 3, 3.1415, 'a', 'frase', [1, 2, 3])


# acessando elementos da tupla (slice / slicing)
## assim como listas, tuplas armazenam sequencias de objetos que podem ser acessados por suas posições
tupla[0]        # mostra primeiro elemento
tupla [-1]      # mostra último elemento
tupla[1:3]      # mostra os elementos dentro do range
tupla[::2]      # mostra todos os elementos em intervalo 2
tupla [:2]      # mostra todos os elementos até o indice 2
tupla [2:]      # mostra todos os elementos a partir do índice 2
tupla [:-1]     # mostra todos os elementoselementos de trás para frente

# tuplas são imutáveis
## isso significa que uma vez criadas, não podemos alterar, adicionar ou remover elementos da mesma

# desempacotamento de tupla
nome, sobrenome, idade = ('bruna', 'andrade', 26)


# tuplas são iteráveis
## por possuir os métodos __iter__ e __getitem__, tuplas podem ser iteradas
for i in tupla:
    print(i)


# convertendo listas para tuplas
list(tupla)


# convertendo tuplas para listas
tuple(lista)


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
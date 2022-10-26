"""
### Dicionário (dict) ###

definição: é um container que armazena elementos/objetos  de forma
não sequencial, mutável e iterável, permitindo valores repetidos, mas não chaves
"""

# criando um dicionário
dicio = {'a': 1, 'b': 2, 'c': 3}

# verificando o tipo
type(dicio)

# criando um dicionario complexo
complex = {
    'inteiro': 8,
    'float': 3.1415,
    'string': "testículo",
    'lista': [1, 2, 3],
    'tupla': (4, 5, 6),
    'dicio': {
        'rua': 'Rua Azul',
        'numero': 75
    } 
}

# acessando os elemento da tupla
## diferente de listas e tuplas, o acesso não é posicional, mas pela chave
complex['dicio']['numero']
complex['lista'].append(4)
complex['dicio']['bairro'] = 'Jardins'

# dicionários são mutáveis
## podemos adicionar e remover elementos, podemos também valores mas não as chaves
complex.pop('inteiro')


# dicionários são iteráveis
for key in complex:
    print(key)

# métodos de dicionário
## novo dicionário de compras contendo item e quantidade

## método keys
compras = {
    'arroz': 1,
    'feijão': 2,
    'chocolate': 3,
}

compras.keys()              # imprime todas as chaves do dicionário
'arroz' in compras.keys()   # booleano se chave existe dentro do dicionário

## método values
compras.values()    # imprime todos os valores do dicionário

## verificando de tem um item no dicionario




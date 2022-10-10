"""
### Conjunto (set) ###

definição: é um container que armazena itens não ordenados/sequenciados, mutáveis e iteráveis
mas sem elementos duplicados.
"""

# criando um conjunto



# verificando o tipo



# criando um conjunto misto



# acessando elementos do conjunto (slice / slicing)
## diferente de listas e tuplas, conjuntos são objetos não sequenciais, ou seja, não tem uma posição
## definida, o que impossibilita realizar o slice.



## realizando a instrospecção do objeto set, observamos que não possui o método __getitem__, logo não temos acesso
## ao slice do objeto



# conjuntos são mutáveis
## podemos adicionar e remover elementos

## método add


## método remove



# conjuntos são iteráveis



# conjuntos remove duplicados



# Operações de conjunto



## interseção


## união


## diferença


## diferença simétrica


## disjunção



"""
Exercício:

1. Gere um conjunto com 20 números aleatórios entre 1 e 25
2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30
3. Calcule:
    3.1. se são conjuntos disjuntos
    3.2. a interseção
    3.3. a união
    3.4. a diferença simétrica
    
Para geração dos números aleatórios, utilize a função nativa do python:

    import random
    random.randint(inicio, fim)

"""

import random

# 1. Gere um conjunto com 20 números aleatórios entre 1 e 25
# 2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30

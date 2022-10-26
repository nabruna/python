"""
### Conjunto (set) ###

definição: é um container que armazena itens não ordenados/sequenciados, mutáveis e iteráveis
mas sem elementos duplicados.
"""

# criando um conjunto
conj = {1, 2, 3, 4, 5}


# verificando o tipo
type(conj)



# criando um conjunto misto
misto = {1, 2, 3, 3.1415, 'a', (1, 2, 3), [1, 2, 3]}


# acessando elementos do conjunto (slice / slicing)
## diferente de listas e tuplas, conjuntos são objetos não sequenciais, ou seja, não tem uma posição
## definida, o que impossibilita realizar o slice.



## realizando a instrospecção do objeto set, observamos que não possui o método __getitem__, logo não temos acesso
## ao slice do objeto
dir(conj)


# conjuntos são mutáveis
## podemos adicionar e remover elementos

## método add
conj.add(6)

## método remove
conj.remove(6)


# conjuntos são iteráveis
for i in conj:
    print(i)


# conjuntos remove duplicados
lista = [1, 2, 3, 4, 3, 5, 6, 2, 6, 7, 8, 1, 9, 10]
set(lista)

# Operações de conjunto
conjA = {1, 2, 3, 4, 5}
conjB = {1, 3, 5, 7, 9}


## interseção
conjA.intersection(conjB)

## união
conjA + conjB

## diferença
conjA - conjB

## diferença simétrica
conjA.symmetric_difference(conjB)

## disjunção
conjA.isdisjoint(conjB)

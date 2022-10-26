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
rand1 = random.sample(range(1, 25), 20)
set1 = set(rand1)
print(set1)

# 2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30
rand2 = random.sample(range(5, 30), 20)
set2 = set(rand2)
print(set2)

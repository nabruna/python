"""
Exercício

Dada a lista a seguir:

```python
valores = [23, 18, 45, 78, 55, 64, 16]
```

Crie um script Python que informe qual a posição do **MAIOR** elemento que esta dentro da lista.
"""

valores = [23, 18, 45, 78, 55, 64, 16]
maior_valor = 0

for valor in valores:
    if valor > maior_valor:
        maior_valor = valor

print(maior_valor)
"""
Exercício:

1. Crie uma agenda utilizando dicionário, a agenda deve ter uma lista de 3 contatos.
2. Os contatos, além do nome, devem possuir telefone e email
3. Verifique se há algum contato com o nome 'marcos'
4. altere o telefone do primeiro contato
5. calcule quanto contatos possuem na lista
"""

lista_contatos = {
    'contato1': {
        'nome': 'Aline',
        'tel': 41995876767,
        'email': 'alinesilva@email.com'
    },
        'contato2': {
        'nome': 'Marcos',
        'tel': 41995443322,
        'email': 'marcoslima@email.com'
    },
    'contato3': {
        'nome': 'João',
        'tel': 41999988776,
        'email': 'joaocosta@email.com'
    }
}

for contato in lista_contatos:
    if 'Marcos' in lista_contatos[contato].values():
        print("Marcos está na lista de contatos.")

lista_contatos['contato1']['tel'] = input("Insira o novo telefone de contato: ")

n = 0
for contato in lista_contatos:
    n += 1

print(f"Existem {n} contatos nesta lista.")
# Desempacotamento em chamadas de métodos e funções
string = 'ABCD'
lista = ['José', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'top'
salas = [
    # 0        1
    ['Luís', 'Susana', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luís', 'João', 'Marcos', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Letícia', 'Fabiano', 1, 2, 3, 'Jonathan')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
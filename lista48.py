
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

Listas em Python
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        +0     1    2     3       4
#        -5    -4   -3    -2      -1
lista = [123, 1.2, 'Olá', False, 'Eu denovo']

lista[3]= True

print(lista)


lista2 = [1, 2, 3, 4, 5]
lista2[1] = 20
del lista2[4]
lista2.append('Oi')
valor_removido = lista2.pop(2)
lista2.append(':p')
lista2.insert(0, 'Terrosos')
print(lista2, 'Foi o removido o,',valor_removido)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
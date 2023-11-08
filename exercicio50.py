"""
Exercício
Exiba os índices da lista
0 Luís
1 Oliveira
2 Júnior
"""
lista = ['Luís', 'Oliveira', 'Júnior']
i = 0
lista.append('Susi')

for indice in lista:
    print(f'{i} {indice}')
    i += 1
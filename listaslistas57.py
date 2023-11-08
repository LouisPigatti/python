'''
Listas dentro de listas e seus respectivos índices
'''

#         índice 0             índice 1                  índice 2
salas = [['Luís', 'Joao'], ['Guilherme', 'Victor'], ['Kai', 'Julia',]]

'''
print(salas[1][0])
'''

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)
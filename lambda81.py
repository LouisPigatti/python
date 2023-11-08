# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

#lista =[1, 7, 4, 9, 1, 3]
#lista.sort()
#print(lista)

#def ordena(item):
#    return item['nome']

#lista.sort(key=ordena)  No 'Key' você passa o nome da função que é para ser executada.

#for item in lista:
#    print(item)

lista = [
{'nome': 'Luís', 'sobrenome': 'Pigatti'},
{'nome': 'Sabrina', 'sobrenome': 'Oliveira'},
{'nome': 'João', 'sobrenome': 'Gabriel'},
{'nome': 'Guilherme', 'sobrenome': 'Gravalos'},
{'nome': 'Felipe', 'sobrenome': 'Ferreira'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
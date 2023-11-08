"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []
i = 0

while True:
    print('Escolha uma das opções: ')
    inicio = input('[i]nserir [a]pagar [l]istar: ').lower()

    if inicio == 'i':
        valor = input('Digite o que você deseja adicionar a lista: ')
        lista.append(valor)    
    elif inicio == 'a':
        deletado = input('Digite o item que você deseja deletar: ')
        del lista[deletado]
    elif inicio == 'l':
        ...
    else:
        print('Digite alguma das opcções válidas.')
    
    print(lista)
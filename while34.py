
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

teste = True

while teste:
    nome = input('Qual é o seu nome? ')
    print(f'Seu nome é {nome}.')

    if nome == 'sair':
        break

print('Você saiu do laço!')
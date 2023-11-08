"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    print('O número digitado é inteiro.')
else:
    print('O número digitado não é inteiro.')

if numero.isdigit():
     numero_int = int(numero)
     par_impar = numero_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {numero_int} é {par_impar_texto}')
else:
     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são? ')

try:
    hora = int(horario)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Desconheço esse horário')
except:
    print('Por favor use números inteiros.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual é o seu nome? ')

try:

    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal.')
    elif len(nome) > 6:
        print('Seu nome é muito grande.')
    else:
        print('Ok.')

except:
    print('Você não digitou seu nome.')
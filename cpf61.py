"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# 811.035.360-60

num1 = input('Digite o primeiro digito do seu cpf: ')
num2 = input('Digite o segundo digito do seu cpf: ')
num3 = input('Digite o terceiro digito do seu cpf: ')
num4 = input('Digite o quarto digito do seu cpf: ')
num5 = input('Digite o quinto digito do seu cpf: ')
num6 = input('Digite o sexto digito do seu cpf: ')
num7 = input('Digite o sétimo digito do seu cpf: ')
num8 = input('Digite o oitavo digito do seu cpf: ')
num9 = input('Digite o nono digito do seu cpf: ')

try:
    num1_int = int(num1)
    num2_int = int(num2)
    num3_int = int(num3)
    num4_int = int(num4)
    num5_int = int(num5)
    num6_int = int(num6)
    num7_int = int(num7)
    num8_int = int(num8)
    num9_int = int(num9)
except:
    print('Você não digitou um número.')

num1_mult = num1_int * 10
num2_mult = num2_int * 9
num3_mult = num3_int * 8
num4_mult = num4_int * 7
num5_mult = num5_int * 6
num6_mult = num6_int * 5
num7_mult = num7_int * 4
num8_mult = num8_int * 3
num9_mult = num9_int * 2

soma = num1_mult + num2_mult + num3_mult + num4_mult + num5_mult + num6_mult + num7_mult + num8_mult + num9_mult

multiplicacao = soma * 10

modulo = multiplicacao % 11

print(modulo)
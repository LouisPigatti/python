"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0

while contador < 50:
    contador += 1

    if contador == 5:
        print('O "5" sumiu.')
        continue

    if contador >= 10 and contador <= 25:
        print('sumiu', contador)
        continue

    print(contador)
senha = '123456'
senha_digitada = ''
tentativas = 0

while senha != senha_digitada:

    senha_digitada = input(f'Você tentou {tentativas}x: ')

    tentativas += 1

print(f'Você tentou: {(tentativas)} vezes.')
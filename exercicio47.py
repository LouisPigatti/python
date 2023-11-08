''' Jogo para adivinhar a palavra secreta '''

import os


palavra = 'Perfume'
letras_acertadas = ''
chances = 0

while True:

    letra_digitada = input('Digite uma letra para formar a palavra secreta: ')
    chances += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra: ', palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('Parabéns, você acertou a palavra!')
        print('A palavra secreta era: ', palavra)
        print('Você tentou: ', chances)
        letras_acertadas = ''
        chances = 0
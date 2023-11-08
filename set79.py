letras = set()
chances = 0
import os
while True:
    chances += 1
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if len(letra) > 1:
        print('Digite apenas uma letra. ')
        continue

    if 'l' in letras:
        os.system('cls')
        print('Você acertou a letra!')
        print(f'Essas foram as letras que você tentou {letras}.')
        print(f'Você tentou {chances} vezes.')
        break
    print(letras)
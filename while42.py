frase = 'O Python é uma linguagem multiparadigma. Python foi criado por Guido Van Rossum.'

i = 0
while i < len(frase):
    letras = frase[i]
    quantas_vezes = frase.count(letras)

    print(letras, quantas_vezes)
    i += 1
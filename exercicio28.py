nome = input("Qual é o seu nome? ")
idade = input("Quantos anos você tem? ")

if nome and idade:
    print(f"Seu nome é {nome} e tem {idade} anos.")
    print(f"Seu nome invertido é {nome[::-1]}")
    if ' ' in nome:
        print("Seu nome tem espaços.")
    else:
        print("Seu nome não tem espaços.")
    print(f"Seu nome tem {len(nome)} letras.")        
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Você não preencheu todos os campos.")
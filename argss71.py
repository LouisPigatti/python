def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

        
soma_x = soma(1, 2, 3)
print(soma_x)

# Existe uma função que soma iteráveis:
print(sum([1 + 2]))

numeros = 1, 2, 3, 10, 20
print(*numeros)

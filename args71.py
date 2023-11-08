def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(f"O número é '{numero}' e a soma é '{total}'.")

        
soma(1, 2, 3, 4, 5)
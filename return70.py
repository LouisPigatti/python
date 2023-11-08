'''
Função return, algo que não retorna valor passa a retornar.
'''

def soma(x, y):
    if x > 10:
        return 7
    return x + y

print(soma(11, 8))

#soma1 = soma(2, 4)
#soma2 = soma(7, 1)
# print(soma1 + soma2)
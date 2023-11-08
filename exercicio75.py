def criar_mult(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = criar_mult(2)
triplicar = criar_mult(3)
quadruplicar = criar_mult(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))

''' Eu já tenho um certo conhecimento de Python e esse protótipo eu tirei de um exercicío
    que eu estava fazendo um tempo atrás.
'''
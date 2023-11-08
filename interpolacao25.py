"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.3f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

pergunta1 = input('Qual seu nome? ')
pergunta2 = int(input('Quantos anos você tem? '))
teste = 'Seu nome é %s e tem %i anos' % (pergunta1, pergunta2)
print(teste)
pessoa = {'Nome': 'Luís Felipe', 'Sobrenome': 'Pigatti',
          'Idade': 17, 'Altura': 1.77,
          'Endereços': [{'Casa': 'Av São Paulo'}, {'Escola': 'Senac'}],
          }

#pessoa2 = dict(nome='João', sobrenome='Gabriel')
#print(pessoa2)

print(pessoa, type(pessoa))
print()

print(pessoa['Nome'])
print(pessoa['Sobrenome'])
print()

for item in pessoa:
    print(item, pessoa[item])

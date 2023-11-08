# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {'Nome': 'Luís Felipe', 'Sobrenome': 'Pigatti'}

print(len(pessoa))
print(tuple(pessoa.keys())) #Você pode fazer a coersão para lista também.
print(list(pessoa.values())) #Você pode fazer a coersão para tupla também.
print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

pessoa.setdefault('idade', None) #Com o setdefault criamos uma chave e damos um valor
                                 #para o programa não quebrar
print(pessoa['idade']) #Se tentarmos buscar uma chave que não existe teremos um erro.

print(pessoa.get('idade', 'Não existe esse valor')) #O get tenta buscar um valor, se não
                                                    #existir ele retorna None.

pessoa.update(Nome='Louis', Altura=1.77) #Com o Update criamos e adicionamos items no dicionário.
print(pessoa)
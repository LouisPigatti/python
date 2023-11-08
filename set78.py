# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set('Luís') #Pode vir fora de ordem os valores
s2 = set()  # vazio
s3 = {'Luís', 1, 2, 3}  # com dados

print(s1)
print(s2)
print(s3)
print()

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 4, 4, 4, 4, 4, 1] #O set apaga valores duplicados
s1 = set(l1)
l2 = list(s1)
print(l2)
s3 = {1, 2, 3}
print(5 in s3)
for number in s3:
    print(number)
print()

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luís')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luís')
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)
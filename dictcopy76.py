# Shallow Copy - Cópia rasa para poucas informações
# Deep Copy - Cópia profunda para muitas informações
# Com um módulo conseguimos fazer isso
import copy

d1 = {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}

#d2 = d1.copy()  shallow copy
d2 = copy.deepcopy(d1) # deepcopy

d2['c1'] = 7
d2['l1'][0] = 9

print(d1)
print(d2)
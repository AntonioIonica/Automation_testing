"""
How to find only the duplicates
"""

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = [] # o noua lista unde adaugam duplicatele
for value in some_list:
    if some_list.count(value) > 1:  # cand in lista numaram fiecare valoarea si se gaseste mai mult de o data
        if value not in duplicates: # apoi cand acea valoare nu se gaseste deja in duplicates, o adaugam
            duplicates.append(value)

print(duplicates)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)


# list = transformam in lista cum cere
# set = sa apara fara duplicate
# for x in some_list sa mearga prin lista, if = numai cand count(x) din lista some_list se gaseste mai mult de o data
"""
How to use a variable outside the function
so you can store something outside
"""

total = 0


def plus_one():
    global total  # aici declaram variabila care deja exista global sa aiba acces la ea
    total += 1  # aici ne folosim de variabila total care vina din exteriorul functiei si va tine minte cifra
    return total  # aici returnam valoarea total


plus_one()
plus_one()
print(plus_one())  # mai sus am apelat-o de 2 ori + ultima data cand facem print = 3

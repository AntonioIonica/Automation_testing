"""
How to handle and error
"""

while True: # cat timp e adevarat codul, adica sa ruleze pana devine corect, atat!
    try:
        age = int(input('Please enter your age: '))
        10 / age
    except ValueError:  # aici punem tipul de eroare pe care il vom primi si printul cu ce sa apara
        print('Please enter a value!')
    except ZeroDivisionError: # alta eroare pentru care facem error handling
        print('0 is not allowed!')
    else: # cand nu mai avem o eroare si introducem ceea ce trebuie
        print('Thank you!')
        break

def adding(number1, number2):
    try:
        return number1 + number2
    except (TypeError, ZeroDivisionError) as err:
        return f'The error is {err}'

print(adding('1', 2))
"""
Exercitiu
"""


def check_fields(actual, expected):
    if len(actual) > 0:
        if actual == expected:
            print("Test passed")
        else:
            print("Test failed")
    else:
        print("Field empty")


def mail_check(email):
    if '@' and '.' in email:
        return True
    else:
        print("Wrong email")


def update_form_page(name, surname, email, password, gender):
    _name = input("Enter your name: ")
    _surname = input("Enter your surname: ")
    _email = input("Enter your email: ")
    _password = input("Enter your password: ")
    _gender = input("Enter your gender: ")

    check_fields(name, _name)
    check_fields(surname, _surname)
    if mail_check(_email) and mail_check(email):
        check_fields(email, _email)
    check_fields(password, _password)
    check_fields(gender, _gender)


update_form_page('Pop', '', 'john@doe.com', 'parola', 'male')

# TODO: define a function for checking if pass contains one lowercase, uppercase, special character
# TODO: Bonus: check if pass field does contains spaces
# TODO: Optional: define a class, construct a car.

# if len(_name) > 0:
#     if name == _name:
#         print("Test passed")
#     else:
#         print("Test failed")
# else:
#     print("Field empty")
# #
# if len(_surname) > 0:
#     if surname == _surname:
#         print("Test passed")
#     else:
#         print("Test failed")
# else:
#     print("Field empty")
# ##
# if len(_email) > 0:
#     if email == _email:
#         print("Test passed")
#     else:
#         print("Test failed")
# else:
#     print("Field empty")
# ###
# if len(_password) > 0:
#     if password == _password:
#         print("Test passed")
#     else:
#         print("Test failed")
# else:
#     print("Field empty")
#
# ####
# if len(_gender) > 0:
#     if gender == _gender:
#         print("Test passed")
#     else:
#         print("Test failed")
# else:
#     print("Field empty")

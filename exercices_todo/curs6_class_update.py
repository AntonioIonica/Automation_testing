"""
Form page - Classes
"""


class UpdateFormPage:
    def __init__(self, name, surname, password, email, gender):  # Constructor cu parametri
          # Atribute de instanta

        self._name = name
        self._surname = surname
        self._password = password
        self._email = email
        self._gender = gender

    #    def check_fields(self, actual, expected):
    def check_fields(actual, expected):
        if len(_actual) > 0:
            if _actual == expected:
                print("Test passed")
            else:
                print("Test failed")
        else:
            print("Field empty")

    def mail_check(self):
        if '@' and '.' in self._email:
            return True
        else:
            print("Wrong email")


    def update_form_page(self):
        _name = input("Enter your name: ")
        _surname = input("Enter your surname: ")
        _email = input("Enter your email: ")
        _password = input("Enter your password: ")
        _gender = input("Enter your gender: ")


        self.check_fields()


# Obiect / Instantiere
form_page = UpdateFormPage("Andrei", "Ionut", "parola", "email@dom.com", "male")
form_page.update_form_page()
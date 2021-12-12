"""
FILE IO
"""
from translate import Translator

translator = Translator(to_lang='fr')
try:
    with open('translate.txt', mode='r') as my_file:
        # mode='r+' to read and write
        # mode='w' to write and create a new folder if it doens't exist with specific name
        # mode='a' to read and append
        # print(my_file.read())  # cu read citim textul
        # my_file.seek(0)  # muta cursorul de citit de la 0 pentru ca read va muta cursorul mereu
        # print(my_file.read())
        # print(my_file.readlines())  # sau punem pentru a citi toate liniile
        # my_file.close() nu mai e nevoie sa dai close daca pui with
        text = my_file.read()
        translation = translator.translate(text)
        with open('/test-fr.txt', mode='w') as file_fr:
            file_fr.write(translation)
except FileNotFoundError as err:
    print(f'File not exists!')
    raise err

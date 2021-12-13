"""
regular expression
"""

import re

pattern = re.compile('This')  # daca nu am avea pattern, am trimite in loc de pattern.search, re.search(cuvant, string)
string = 'This is a big string'

a = pattern.search(string)
b = pattern.findall(string)  # de cate ori apare in string
c = pattern.fullmatch(string)  # trebuie sa fie un pattern exact la fel ca stringul
d = pattern.match(string)  # avem un match care compara stringul, dar nu conteaza ce urmeaza dupa

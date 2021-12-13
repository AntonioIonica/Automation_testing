"""
How to validate some password
'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' is for an email
"""

import re

pattern = re.compile(r'([A-Za-z0-9$%#@]{8,}[0-9])')
password = '23423@%@8'
check = pattern.fullmatch(password)
print(check)

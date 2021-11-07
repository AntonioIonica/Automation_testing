"""
sorted by second key with lambda
"""

a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])  # key e parametru egal cu lambda in care x e mereu index[1], adica al doilea item din tuple

print(a)  #printam lista modificata
"""
Christmas tree transforming
"""

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for row in picture:         # trecem prin fiecare rand, adica lista
  for pixel in row:         # trecem prin fiecare caracter din rand
    if (pixel == 1):
      print('*', end ="")   # end = "" apare aici ca default e noua linie print, dar "" inseamna ca totul apare legat
    else:
      print(' ', end ="")
  print('')                 # identarea e in interiorul primului for, adica row in picture, practic la fiecare
                            # lista avem un empty string care sa ne dea o noua linie
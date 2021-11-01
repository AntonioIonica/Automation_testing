import random

random.seed(1)

state = random.getstate()

for i in range(3):
    print(random.randint(1, 1000))

random.setstate(state)
for i in range(3):
    print(random.randint(1, 1000))
import sys
import random

n, max_ai = map(int, sys.argv[1:3])
random.seed(int(sys.argv[-1]))
s = []


def get_random():
    return random.randint(1, max_ai)


def get_index():
    return random.randint(0, len(s) - 1)

print(n)

for i in range(n):
    im = i % 5
    if im <= 2:
        x = get_random()
        s.append(x)
        print(f'+ {x}')
    elif im == 3:
        print(f'? {get_random()}')
    elif im == 4:
        x = get_index()
        print(f'- {s[x]}')
        s.pop(x)


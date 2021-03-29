import sys
import random
n = int(sys.argv[1])
random.seed(int(sys.argv[2]))
x = [i+1 for i in range(n)]
random.shuffle(x)
print(n)
print(*x, sep=' ')
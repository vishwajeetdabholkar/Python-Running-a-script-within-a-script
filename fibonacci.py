import sys

n = int(sys.argv[1])

x = 0
y = 1

for i in range(0, n):
    x = x + y
    y = x - y
    print(x)
    
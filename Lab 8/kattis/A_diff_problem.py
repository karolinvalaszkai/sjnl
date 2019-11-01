import sys


"Compute the difference between non-negative integers."

for row in sys.stdin:   #standard input
    xy = row.split()
    x = int(xy[0])
    y = int(xy[1])
    print(abs(x - y))
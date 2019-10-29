import sys

for row in sys.stdin:
    xy = row.split()
    x = int(xy[0])
    y = int(xy[1])
    print(abs(x - y))
import sys
input = sys.stdin.readline

s = [0] * 10001
s[0] = 1
s[1] = 1

for i in range(2,10001):
    if s[i] == 0:
        for j in range(i+i,10001,i):
            s[j] = 1

t = int(input())

for _ in range(t):
    n = int(input())
    result = 10001
    x = 0
    y = 0
    for i in range(2,n):
        if s[i] == 0 and s[n-i] == 0:
            if result > abs(i-(n-i)):
                x = i
                y = n-i
                result = abs(i - (n - i))
    if x < y:
        print("%d %d"%(x,y))
    else:
        print("%d %d" % (y, x))
import sys

input = sys.stdin.readline

n = int(input())

r = 0
b = 0
if n == 1:
    r = 1
else:
    r =1
    n-=1
    b = 6
    while n > 0:
        n -= b
        r +=1
        b +=6

print(r)
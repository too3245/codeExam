import sys

input = sys.stdin.readline

n = int(input())

s = 2
while n > 1:
    if n % s == 0:
        n = n // s
        print(s)
    else:
        s+=1
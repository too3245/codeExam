import sys

input = sys.stdin.readline

n = int(input())

def sol(n,a,b,c):
    if n == 1:
        print(a,c)
    else:
        sol(n-1,a,c,b)
        print(a,c)
        sol(n-1,b,a,c)
sum = 1

for i in range(n-1):
    sum = sum * 2 + 1

print(sum)
sol(n,1,2,3)
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    a = []
    for i in range(1,n+1):
        a.append(i)

    for i in range(k):
        for j in range(1,n):
            a[j] += a[j-1]
    print(a[n-1])

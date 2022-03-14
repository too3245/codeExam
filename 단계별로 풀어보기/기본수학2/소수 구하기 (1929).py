import sys

input = sys.stdin.readline

n, m = map(int,input().split())

s = [0] * (m+1)
s[0] = 1
s[1] = 1
for i in range(2,m+1):
    if s[i] == 0:
        for j in range(i+i,m+1,i):
            s[j] = 1

for i in range(n,m+1):
    if s[i] == 0:
        print(i)
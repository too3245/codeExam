import sys

input = sys.stdin.readline

n,m = map(str,input().split())

n = n[::-1]
m = m[::-1]

result = 0

if int(n) > int(m):
    result = int(n)
else:
    result = int(m)

print(result)
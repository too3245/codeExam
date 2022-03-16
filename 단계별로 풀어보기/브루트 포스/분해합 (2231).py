import sys

input = sys.stdin.readline

n = int(input())
s = [0] * (n+1)
for i in range(n):
    k = 0
    for j in str(i):
        k += int(j)
    if (i+k) > n:
        continue
    if s[i+k] == 0:
        s[i+k] = i

print(s[n])
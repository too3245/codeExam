import sys

input = sys.stdin.readline

n = int(input())

count = 0
for _ in range(n):
    s = str(input().strip())
    ar = {}
    for i in range(len(s)):
        if i > 0 and s[i] != s[i-1] and ar.get(s[i]) is not None:
            break
        else:
            ar[s[i]] = i
    else:
        count +=1
print(count)
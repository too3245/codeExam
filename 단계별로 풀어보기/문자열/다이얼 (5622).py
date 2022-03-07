import sys

input = sys.stdin.readline

n = input().strip()
s = ["","","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

sum = 0
for i in range(len(s)):
    for j in s[i]:
        for k in n:
            if k == j:
                sum +=i
print(sum)
import sys

input = sys.stdin.readline

n = str(input().strip().upper())

a = {}

result = ''
count = 0
for i in n:
    a[i] = 0
for i in n:
    a[i] += 1


for i in a:
    if count < a[i]:
        result = i
        count = a[i]
    elif count == a[i]:
        result = '?'

print(result)
import sys

input = sys.stdin.readline

a, b, c = map(int,input().split())

result = a / (c-b)
if result <= 0:
    result = -1
else:
    result +=1
print(int(result))
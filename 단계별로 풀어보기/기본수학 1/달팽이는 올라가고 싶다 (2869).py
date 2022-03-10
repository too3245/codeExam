import sys

input = sys.stdin.readline

a, b, v = map(int,input().split())

result =  (v - b) / (a - b)
if result == int(result) :
    result = int(result)
else:
    result = int(result) +1
print(result)
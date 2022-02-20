import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = a*b
j = 10
b_str = str(b)[::-1]
for i in b_str:
    bn = int(i)
    print(a*bn)
print(c)
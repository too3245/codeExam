import sys

input = sys.stdin.readline

a, b, c = map(int,input().split())
m = 0
if a == b and a == c and b == c:
    m = 10000 + (a*1000)
elif a == b and a != c or a == c and b != c:
    m = 1000 + (a * 100)
elif b == c and a != b:
    m = 1000 + (b*100)
else:
    m = max(a,b,c) * 100

print(m)
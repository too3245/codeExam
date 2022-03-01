import sys

input = sys.stdin.readline

n,x = map(int,input().split())

a = list(map(int,input().split()))

for i in a:
    if x > i:
        print(i,end=" ")
print()
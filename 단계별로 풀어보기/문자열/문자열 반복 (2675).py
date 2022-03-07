import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r,s = map(str,input().split())
    for i in s:
        for _ in range(int(r)):
            print(i,end="")
    print()
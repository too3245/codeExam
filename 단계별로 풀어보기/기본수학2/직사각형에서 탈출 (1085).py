import sys

input = sys.stdin.readline

x,y,w,h = map(int,input().split())

num = min(x,y,(w-x),(h-y))
print(num)
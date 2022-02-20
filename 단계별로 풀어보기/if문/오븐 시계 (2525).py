import sys

input = sys.stdin.readline

h, m = map(int,input().split())
n = int(input())

min_total = m + n

hour_out = (h + (min_total // 60)) % 24
min_out = min_total % 60

print("%d %d"%(hour_out,min_out))
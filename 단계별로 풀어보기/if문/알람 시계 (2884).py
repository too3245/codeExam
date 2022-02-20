import sys
input = sys.stdin.readline

h, m = map(int,input().split())

hour_out = 0
min_out = 0

if (m-45) < 0:
    min_out = 60 + (m-45)
    hour_out = h - 1
else:
    hour_out = h
    min_out = m - 45

if hour_out == -1:
    hour_out = 23

print("%d %d"%(hour_out,min_out))

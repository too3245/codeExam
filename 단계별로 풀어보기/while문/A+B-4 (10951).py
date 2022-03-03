import sys

input = sys.stdin.readline

n = 0

while True:
    try:
        x,y = map(int,input().split())

        if 0 < x < 10 and 0 < y < 10:
            print(x+y)
        else:
            break
    except:
        break
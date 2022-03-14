import sys

input =sys.stdin.readline

x_list = []
y_list = []

for _ in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

x = 0
y = 0

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print("%d %d"%(x,y))
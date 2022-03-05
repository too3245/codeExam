import sys

input = sys.stdin.readline

n = []

for _ in range(9):
    n.append(int(input()))

max_num = -217400000
count = 0
for i in range(9):
    if max_num < n[i]:
        max_num = n[i]
        count = i+1

print(max_num)
print(count)
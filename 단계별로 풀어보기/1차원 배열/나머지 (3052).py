import sys

input = sys.stdin.readline

n = [0] * 42
count = 0
for _ in range(10):
    n[int(input())%42] += 1

for i in n:
    if i != 0:
        count +=1

print(count)
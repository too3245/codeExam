import sys

input = sys.stdin.readline

n = int(input())

n_list = input().strip()

sum = 0

for i in n_list:
    sum += int(i)

print(sum)
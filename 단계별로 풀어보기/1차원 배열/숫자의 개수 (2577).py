import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
sum_num = str(a * b * c)
count = [0] * 10
for i in range(10):
    for j in sum_num:
        if str(i) == j:
            count[i] += 1

for i in count:
    print(i)
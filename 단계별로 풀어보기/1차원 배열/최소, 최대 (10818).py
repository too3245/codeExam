import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

min_num = 2147000000
max_num = -2147000000

for i in range(n):
    if min_num > n_list[i]:
        min_num = n_list[i]
    if max_num < n_list[i]:
        max_num = n_list[i]

print("%d %d"%(min_num,max_num))
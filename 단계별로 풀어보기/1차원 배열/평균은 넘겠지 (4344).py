import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n_list = list(map(int,input().split()))
    e = n_list[0]
    e_list = n_list[1:]
    avg = sum(e_list) / e
    e_count = 0
    for i in e_list:
        if avg < i:
            e_count +=1
    print("%.3f%%" % ((e_count / e)*100))
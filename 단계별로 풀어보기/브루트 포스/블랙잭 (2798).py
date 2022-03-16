import sys
input = sys.stdin.readline


n, m = map(int,input().split())

n_list = list(map(int,input().split()))
num = 0
last = m
min = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            min = m - (n_list[i] + n_list[j] + n_list[k])
            if min >= 0:
                if min < last:
                    last = min
                    num = n_list[i] + n_list[j] + n_list[k]
print(num)
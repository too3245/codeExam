'''
1. 아이디어
    - N이상 M이하의 소수 구하기
    - N +  M 출력
    - 최솟값 출력
    - 소수가 없는경우는 -1 출력.
2. Big(O)
    10000 O(M-N)
3. 자료구조
    LIST
'''

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

s_list = [0] * (m+1)
s_list[0] = 1
s_list[1] = 1

for i in range(2,m+1):
    if s_list[i] == 0:
        for j in range(i+i,m+1,i):
            s_list[j] = 1

sum_num = 0
min_num = 10001

for i in range(n,m+1):
    if s_list[i] == 0:
        if min_num > i:
            min_num = i
        sum_num += i

if min_num == 10001:
    print(-1)
else:
    print(sum_num)
    print(min_num)
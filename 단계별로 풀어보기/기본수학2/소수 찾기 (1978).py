'''
1. 아이디어
    - 소수는 자기자신과 1밖에 없는 경우
    - 자기자신의 숫자 * 로 증가하는 숫자
    - 갯수 세기 끝.
2, Big(O)
    1000 개를 미리구하면 O(N)이됨
3. 자료구조
    LIST[1001]
'''
import sys

input = sys.stdin.readline

s = [0] * 1001
s[0] = 1
s[1] = 1
n = int(input())
num_list = list(map(int,input().split()))
for i in range(1,1001):
    if s[i] == 0:
        for j in range(i*i,1001,i):
            s[j] = 1

count = 0
for i in num_list:
    if s[i] == 0:
        count +=1
print(count)

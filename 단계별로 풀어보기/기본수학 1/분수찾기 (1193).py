'''
1 line 1 -> 1/1 홀
2 line 2,3 -> 1/2, 2/1 짝
3 line 4,5,6 -> 3/1, 2/2, 1/3 홀
4 line 7,8,9,10 -> 1/4, 2/3, 3/2, 4/1 짝

'''
import sys

input = sys.stdin.readline

n = int(input())

l = 0
i = 0

while n > i:
    l +=1
    i +=l

diff = i - n
top = 0
bottom = 0
if l % 2 == 0:
    top = l - diff
    bottom = diff +1
else:
    top = diff + 1
    bottom = l - diff

print(str(top)+'/'+str(bottom))
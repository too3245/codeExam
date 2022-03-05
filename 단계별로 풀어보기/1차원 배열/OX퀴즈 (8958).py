import sys

input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    q = list(map(str,input()))
    num = 0
    for i in q:
        if i == 'O':
            num += 1
            count += num
        else:
            num = 0
    print(count)
    count = 0
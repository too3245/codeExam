import sys
input = sys.stdin.readline

n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += n // 5
        break
    n -= 3
    count +=1
else:
    count = -1

print(count)
import sys

input = sys.stdin.readline

n = int(input())
old_num = n
count = 0
while True:
    count +=1
    left_num = n % 10
    right_num = ((n%10) + (n//10)) % 10
    n = left_num * 10 + right_num
    if n == old_num:
        break

print(count)
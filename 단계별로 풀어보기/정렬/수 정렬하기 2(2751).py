import sys

input = sys.stdin.readline
sys.setrecursionlimit(2000000000)


def sol(n):

    if len(n) <= 1:
        return n

    mid = len(n) //2
    left = n[:mid]
    right = n[mid:]

    left1 = sol(left)
    right2 = sol(right)
    return merge(left1,right2)


def merge(left,right):

    i = 0
    j = 0
    sort_l = []

    while (i < len(left)) and (j< len(right)):
        if left[i] < right[j]:
            sort_l.append(left[i])
            i += 1
        else:
            sort_l.append(right[j])
            j += 1


    while i < len(left):
        sort_l.append(left[i])
        i+=1

    while j < len(right):
        sort_l.append(right[j])
        j += 1



    return sort_l

n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))

s = sol(l)

for i in s:
    print(i)
import sys
input =sys.stdin.readline

s = [0] * (123457 * 2)

s[0] = 1
s[1] = 1
for i in range(2,123457 * 2):
    if s[i] == 0:
        for j in range(i+i,123457*2,i):
            s[j] = 1

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1,(2 * n)+1):
        if s[i] == 0:
            count +=1
    print(count)


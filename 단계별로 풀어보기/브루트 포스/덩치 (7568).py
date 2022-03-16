import sys
input = sys.stdin.readline

rank = 1
currentRank = 1
n = int(input())
m = []
r = []
for _ in range(n):
    x, y = map(int,input().split())
    m.append((x,y))

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if m[i][0] < m[j][0] and m[i][1] < m[j][1]:
            rank +=1
    r.append(rank)

for i in r:
    print(i,end=' ')
print()


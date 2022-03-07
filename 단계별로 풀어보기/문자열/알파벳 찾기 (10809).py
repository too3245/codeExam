import sys

input = sys.stdin.readline

n = input().strip()
alpha = [-1] * 26
for i in range(len(n)):
    number = ord(n[i]) - 97
    if alpha[number] == -1:
        alpha[number] = i

for i in alpha:
    print(i,end=" ")
print()
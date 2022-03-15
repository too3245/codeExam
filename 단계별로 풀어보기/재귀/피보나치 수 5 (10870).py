import sys

input = sys.stdin.readline

def sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1


    return sol(n-1) + sol(n-2)


if __name__ == "__main__":
    num = 0
    n = int(input())

    num = sol(n)
    print(num)

import sys

input = sys.stdin.readline


def sol(sum,i,j):
    global num
    if i < j:
        num = sum
        return

    sol(sum*j,i,j+1)



if __name__ == "__main__":
    n = int(input())
    num = 0
    sol(1,n,1)
    print(num)
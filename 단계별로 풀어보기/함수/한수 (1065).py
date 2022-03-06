import sys

input = sys.stdin.readline



def solve(number):
    global count
    num_first = int(str(number)[0])

    num_second = 0
    if number > 10:
        num_second = int(str(number)[1])
    diff = num_first - num_second

    if number > 99:
        num_count = len(str(number))
        for i in range(num_count-1):
            if diff != int(str(number)[i]) - int(str(number)[i+1]):
                return

    count +=1

if __name__ == "__main__":
    number = int(input())
    count = 0
    for i in range(1,number+1):
        solve(i)
    print(count)

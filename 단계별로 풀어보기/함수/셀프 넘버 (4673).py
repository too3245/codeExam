'''
1. 아이디어
    1. 10000의 배열로 두고 n+n앞+n뒤의 값을 넣는다.
    2. 이미 있는값이면 continue로 넘긴다.
'''


nums = [0] * 10001


def selfNumber(num):
    array_num = num
    for i in str(num):
        array_num += int(i)
    if array_num > 10000:
        return
    nums[array_num] = 1


if __name__ == "__main__":

    for i in range(1,10000):
        selfNumber(i)

    for i in range(1,10000):
        if nums[i] == 0:
            print(i)

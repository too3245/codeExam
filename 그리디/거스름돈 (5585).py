'''
1.아이디어
- 세탁소 사장 동혁과 동일한 해결방안을 지니고 있다.
- 기본적으로 1000엔 지폐를 제출했을때 N을 빼서 나온수에서
- 500엔, 100엔 10엔 5엔 1엔순으로 나머지를 구한다.
'''


if __name__ == "__main__":
    money = 1000
    n = int(input())
    other = money - n
    coin = [500,100,50,10,5,1]
    count = 0
    for c in coin:
        count += other // c
        other = other % c

    print(count)

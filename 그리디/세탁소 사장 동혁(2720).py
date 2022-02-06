'''
1. 아이디어
- 첫 번째는 각 테스트의 반복 횟수이다.
- 각 금액은 쿼터(0.25) 다임(0.10) 니켈(0.05) 페니(0.01) 이 주어진다.
- 최소의 금액을 배출하라.

2. 시간 복잡도
4 * a
'''
import sys


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        money = int(input())
        coins = [25,10,5,1]

        for coin in coins:
            response_money = money // coin
            money = money % coin
            print(response_money,end=' ')
        print()
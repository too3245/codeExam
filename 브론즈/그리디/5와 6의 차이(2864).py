'''
1.아이디어
- 문자열로 리스트 형태로 문자를 입력 받는다.
- 양측의 6은 5로 변환한다.
- 양측의 5는 6으로 변환한다.
- 큰 숫자에서 작은 숫자를 뺀다.
'''
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n,m = map(str,input().split())

    min_num_n = int(n.replace('6','5'))
    max_num_n = int(n.replace('5','6'))

    min_num_m = int(m.replace('6','5'))
    max_num_m = int(m.replace('5','6'))

    print(min_num_n + min_num_m,max_num_n + max_num_m)
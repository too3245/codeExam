'''
1.아이디어
- 점수 얻는 방법
- (가위(0)+1) % 3 == 바위(1) 형태는 +2
- 가위(0) == 가위 형태는 +1
- row를 먼저 실행하는 반복으로 최대 점수를 얻는 방법을 구한다.
2.BigO
3.데이터타입
'''


if __name__ =="__main__":
    r = int(input())
    play_list = list(map(str,input()))
    n = int(input())
    friend_list = [list(map(str,input())) for _ in range(n)]
    rsp = {'R':0,'S':1,'P':2}
    cs = ms = 0
    for i in range(r):
        ts = [[0,'R'],[0,'S'],[0,'P']]
        for j in range(n):
            if (rsp[play_list[i]]+1) % 3 == rsp[friend_list[j][i]]: cs += 2
            elif play_list[i] == friend_list[j][i]: cs +=1

            for t in ts:
                if (rsp[t[1]]+1) %3 == rsp[friend_list[j][i]]: t[0] +=2
                elif t[1] == friend_list[j][i]: t[0] +=1

        ms +=max(ts)[0]

    print(cs)
    print(ms)


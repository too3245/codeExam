'''
1.아이디어
- S = 1
- LL = 1 LAST +1
'''


if __name__ == "__main__":
    n = int(input())
    strList = list(map(str,input()))
    res = 0
    cpt = 0
    for i in range(n):
        if strList[i] == 'L':
           cpt +=1

    if cpt == 0:
        res = n
    else:
        res = n - (cpt//2)+1
    print(res)

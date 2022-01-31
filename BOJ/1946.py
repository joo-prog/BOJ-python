import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    score=[]
    for _ in range(n):
        score.append(list(map(int, input().split())))
    score.sort()
    num=score[0][1]
    cnt=1
    for i in range(1, n):
        if score[i][1]<num:
            cnt+=1
            num=score[i][1]
            if score[i][1]==1:
                break
    print(cnt)
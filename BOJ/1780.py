import sys
input=sys.stdin.readline

n=int(input())
paper=[]
for _ in range(n):
    paper.append(list(map(int, input().split())))

cnt1, cnt2, cnt3 = 0, 0, 0

def check(r, c, n):
    global cnt1, cnt2, cnt3
    tmp=paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j]!=tmp:
                for i in range(3):
                    for j in range(3):
                        check(r+i*(n//3), c+j*(n//3), n//3)
                return
    if tmp==-1:
        cnt1+=1
    elif tmp==0:
        cnt2+=1
    else:
        cnt3+=1

check(0, 0, n)
print(f'{cnt1}\n{cnt2}\n{cnt3}')
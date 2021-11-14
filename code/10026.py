import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
li=[]
visited1=[[0]*n for _ in range(n)]
visited2=[[0]*n for _ in range(n)]

for _ in range(n):
    li.append(list(input().strip('\n')))

cnt1=0
cnt2=0
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def rgb1(x, y):
    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        if (0<=tmp_x<n)and(0<=tmp_y<n) and visited1[tmp_x][tmp_y]==0:
            if li[x][y]==li[tmp_x][tmp_y]:
                visited1[tmp_x][tmp_y]=1
                rgb1(tmp_x, tmp_y)

def rgb2(x, y):
    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        if 0<=tmp_x<n and 0<=tmp_y<n and visited2[tmp_x][tmp_y]==0:
            if li[x][y]=='R' or li[x][y]=='G':
                if li[tmp_x][tmp_y]=='R' or li[tmp_x][tmp_y]=='G':
                    visited2[tmp_x][tmp_y]=1
                    rgb2(tmp_x, tmp_y)
            elif li[x][y]==li[tmp_x][tmp_y]:
                visited2[tmp_x][tmp_y]=1
                rgb2(tmp_x, tmp_y)

for i in range(n):
    for j in range(n):
        if visited1[i][j]==0:
            visited1[i][j]=1
            cnt1+=1
            rgb1(i, j)
        if visited2[i][j]==0:
            visited2[i][j]=1
            cnt2+=1
            rgb2(i, j)
            
print(cnt1, cnt2)
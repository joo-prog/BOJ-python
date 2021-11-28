import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx=[-1, -1, -1, 0, 0, 1, 1, 1]
dy=[-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x):
    global n, m
    for i in range(8):
        tmp_y=y+dy[i]
        tmp_x=x+dx[i]
        if 0<=tmp_x<n and 0<=tmp_y<m and li[tmp_y][tmp_x]==1:
            li[tmp_y][tmp_x]=0
            dfs(tmp_y, tmp_x)

while True:
    n, m=map(int,input().split())
    if n==0 and m==0:
        break
    li=[]
    for i in range(m):
        li.append(list(map(int, input().split())))
    
    cnt=0
    for i in range(m):
        for j in range(n):
            if li[i][j]==1:
                li[i][j]=0
                cnt+=1
                dfs(i, j)
    print(cnt)
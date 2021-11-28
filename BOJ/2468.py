import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
max_h=0
li=[]
for i in range(n):
    li.append(list(map(int, input().split())))
    tmp=max(li[i])
    if tmp>=max_h:
        max_h=tmp

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(i, j, h):
    global n
    for k in range(4):
        tmp_x=j+dx[k]
        tmp_y=i+dy[k]
        if 0<=tmp_x<n and 0<=tmp_y<n and visited[tmp_y][tmp_x]==0:
            if li[tmp_y][tmp_x]>h:
                visited[tmp_y][tmp_x]=1
                dfs(tmp_y, tmp_x, h)

max_cnt=0
for h in range(0, max_h+1):
    cnt=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if li[i][j]>h and visited[i][j]==0:
                visited[i][j]=1
                cnt+=1
                dfs(i, j, h)
    max_cnt=max(cnt, max_cnt)
print(max_cnt)
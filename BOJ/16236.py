import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
matrix=[]
fish=[[] for _ in range(7)]
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j]==9:
            x, y=i, j
            matrix[i][j]=0
        elif matrix[i][j]!=0:
            fish[matrix[i][j]].append([i, j])


dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]

time=0
size=2
q=deque()

def bfs(x, y):
    q=deque()
    q.append([x, y, 0])
    min_list=[]
    visited=[[0]*n for _ in range(n)]
    visited[x][y]=1
    min_dist=int(1e9)
    while q:
        x, y, d=q.popleft()
        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            if 0<=tmp_x<n and 0<=tmp_y<n and matrix[tmp_x][tmp_y]<=size and visited[tmp_x][tmp_y]==0:
                visited[tmp_x][tmp_y]=1
                if 0<matrix[tmp_x][tmp_y]<size:
                    min_dist=d
                    min_list.append([d+1, tmp_x, tmp_y])
                elif d+1<=min_dist:
                    q.append([tmp_x, tmp_y, d+1])
    if len(min_list)!=0:
        min_list.sort()
        return min_list[0]
    else:
        return -1
cnt_tmp=0
while True:
    res=bfs(x, y)
    if res==-1:
        break
    x, y=res[1], res[2]
    time+=res[0]
    cnt_tmp+=1
    if size==cnt_tmp:
        size+=1
        cnt_tmp=0
    matrix[x][y]=0

print(time)
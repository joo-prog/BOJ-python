import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
matrix=[]

for i in range(n):
    matrix.append(list(map(int, input().split())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
max_zero=0

def bfs():
    global max_zero
    q=deque()
    tmp_cnt=0
    copy_matrix=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_matrix[i][j]=matrix[i][j]
            if matrix[i][j]==2:
                q.append([i, j])
    while q:
        x, y=q.popleft()
        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            if 0<=tmp_x<n and 0<=tmp_y<m:
                if copy_matrix[tmp_x][tmp_y]==0:
                    copy_matrix[tmp_x][tmp_y]=2
                    q.append([tmp_x, tmp_y])

    for i in range(n):
        for j in range(m):
            if copy_matrix[i][j]==0:
                tmp_cnt+=1
    if max_zero<tmp_cnt:
        max_zero=tmp_cnt


def wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][j]=1
                wall(cnt+1)
                matrix[i][j]=0

wall(0)
print(max_zero)
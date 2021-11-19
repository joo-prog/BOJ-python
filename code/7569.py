import sys
from collections import deque
input=sys.stdin.readline

q=deque()
m, n, h=map(int, input().split())
tomato=[]
for i in range(n*h):
    tomato.append(list(map(int, input().split())))

    for j in range(m):
        if tomato[i][j]==1:
            q.append([j, i, 0])

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
max_day=0
flag=0
def bfs():
    global flag, max_day
    while q:
        x, y, z=q.popleft()
        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            floor=y//n+1
            if 0<=tmp_x<m and n*(floor-1)<=tmp_y<n*floor and tomato[tmp_y][tmp_x]==0:
                flag=1
                max_day=max(max_day, z+1)
                tomato[tmp_y][tmp_x]=1
                q.append([tmp_x, tmp_y, z+1])
        tmp_y=y+n
        if tmp_y<n*h and tomato[tmp_y][x]==0:
            flag=1

            max_day=max(max_day, z+1)
            tomato[tmp_y][x]=1
            q.append([x, tmp_y, z+1])
        tmp_y=y-n
        if 0<=tmp_y and tomato[tmp_y][x]==0:
            flag=1

            max_day=max(max_day, z+1)
            tomato[tmp_y][x]=1
            q.append([x, tmp_y, z+1])

bfs()
for i in range(n*h):
    for j in range(m):
        if tomato[i][j]==0:
            print(-1)
            exit(0)
if flag==0:
    print(0)
else:
    print(max_day)
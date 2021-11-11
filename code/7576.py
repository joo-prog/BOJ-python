from collections import deque
import sys
input=sys.stdin.readline

q=deque()
m, n=map(int, input().split())
tomato=[]
for i in range(n):
    tomato.append(list(map(int, input().split())))

    for j in range(m):
        if tomato[i][j]==1:
            q.append([i, j, 0])

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
            if (tmp_x>=0)and(tmp_x<n)and(tmp_y>=0)and(tmp_y<m) and tomato[tmp_x][tmp_y]==0:
                flag=1
                max_day=max(max_day, z+1)
                tomato[tmp_x][tmp_y]=1
                q.append([tmp_x, tmp_y, z+1])
bfs()
for i in range(n):
    for j in range(m):
        if tomato[i][j]==0:
            print(-1)
            exit(0)
if flag==0:
    print(0)
else:  
    print(max_day)

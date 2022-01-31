import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
g=[]
for _ in range(n):
    g.append(list(map(int, input().strip())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs():
    q=deque()
    q.append([0, 0, 1])
    visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1]=1
    while q:
        x, y, z=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        for i in range(4):
            tmpx=x+dx[i]
            tmpy=y+dy[i]
            if 0<=tmpx<n and 0<=tmpy<m:
                if g[tmpx][tmpy]==1 and z==1:
                    visited[tmpx][tmpy][0]=visited[x][y][z]+1
                    q.append([tmpx, tmpy, 0])
                elif g[tmpx][tmpy]==0 and visited[tmpx][tmpy][z]==0:
                    visited[tmpx][tmpy][z]=visited[x][y][z]+1
                    q.append([tmpx, tmpy, z])
    return -1

print(bfs())
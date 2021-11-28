import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
li=[]
for i in range(n):
    li.append(list(map(int, input().strip())))

q=deque()
dx=[-1, 1, 0, 0]
dy=[0,0,-1,1]
min_num=n*m

def bfs():
    global n, m, min_num
    while q:
        x, y, z=q.popleft()
        if x==m-1 and y==n-1:
            min_num=min(min_num, z)
            continue
        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            if 0<=tmp_x<m and 0<=tmp_y<n and li[tmp_y][tmp_x]==1:
                li[tmp_y][tmp_x]=0
                q.append([tmp_x, tmp_y, z+1])
    return min_num

q.append([0,0, 1])
li[0][0]=0
print(bfs())
import sys
from collections import deque
# sys.setrecursionlimit(10**6) 이거 붙여서 계속 메모리초과 난거임....pypy3쓸때는 주의 이거 함부로 쓰지 말 것
input=sys.stdin.readline

n, l, r=map(int, input().split())
country=[list(map(int, input().split())) for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y):
    global sum
    visited[x][y]=1
    sum+=country[x][y]
    q.append([x, y])

    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        if 0<=tmp_x<n and 0<=tmp_y<n:
            dif=abs(country[tmp_x][tmp_y]-country[x][y])
            if l<=dif<=r and visited[tmp_x][tmp_y]==0:
                dfs(tmp_x, tmp_y)

flag=1
day=-1
while flag==1:
    flag=0
    day+=1
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                q=deque()
                sum=0
                dfs(i, j)
                if len(q)==1:
                    continue
                flag=1
                for x, y in q:
                    country[x][y]=sum//len(q)

print(day)
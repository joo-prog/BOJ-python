from collections import deque
n, m=map(int, input().split())
list=[list(map(int, input())) for i in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

queue=deque()
queue.append([0, 0])

while queue:
    x, y=queue.popleft()
    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        
        if 0<=tmp_x<m and 0<=tmp_y<n:
            if list[tmp_y][tmp_x]==1:
                list[tmp_y][tmp_x]=list[y][x]+1
                queue.append([tmp_x, tmp_y])

print(list[n-1][m-1])
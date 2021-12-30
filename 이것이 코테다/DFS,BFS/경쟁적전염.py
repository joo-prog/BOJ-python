from collections import deque
n, k= map(int ,input().split())
matrix=[]
tmp=[]

for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j]!=0:
            tmp.append(((matrix[i][j], i, j, 0)))
s, x, y=map(int, input().split())
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
tmp.sort()
q=deque(tmp)
while q:
    virus, xx, yy, second=q.popleft()
    if second==s:
        break
    for i in range(4):
        tmp_x=xx+dx[i]
        tmp_y=yy+dy[i]
        if 0<=tmp_x<n and 0<=tmp_y<n:
            if matrix[tmp_x][tmp_y]==0:
                matrix[tmp_x][tmp_y]=matrix[xx][yy]
                q.append([virus, tmp_x, tmp_y, second+1])

print(matrix[x-1][y-1])

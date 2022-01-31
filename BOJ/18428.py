from collections import deque
n=int(input())
matrix=[]

for i in range(n):
    matrix.append(list(input().split()))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

ts='YES'
flag=0

def bfs():
    global ts
    q=deque()
    copy_matrix=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy_matrix[i][j]=matrix[i][j]
            if matrix[i][j]=='T':
                q.append([i, j])
    
    while q:
        x, y=q.popleft()
        
        for i in range(4):
            tmp_x=x
            tmp_y=y
            while True:
                tmp_x=tmp_x+dx[i]
                tmp_y=tmp_y+dy[i]
                if 0<=tmp_x<n and 0<=tmp_y<n:
                    if copy_matrix[tmp_x][tmp_y]=='S':
                        ts='NO'
                        return
                    elif copy_matrix[tmp_x][tmp_y]=='O':
                        break
                else:
                    break

def wall(cnt):
    global ts, flag
    if cnt==3:
        ts='YES'
        bfs()
        return
    for i in range(n):
        for j in range(n):
            if matrix[i][j]=='X':
                matrix[i][j]='O'
                wall(cnt+1)
                
                if ts=='YES':
                    flag=1
                matrix[i][j]='X'
            
wall(0)
if flag==1:
    print('YES')
else:
    print('NO')
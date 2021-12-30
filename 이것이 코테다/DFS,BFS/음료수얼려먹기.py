n, m=map(int, input().split())
list=[list(input().strip()) for i in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        if 0<=tmp_x<m and 0<=tmp_y<n:
            if list[tmp_y][tmp_x]=='0':
                list[tmp_y][tmp_x]='1'
                dfs(tmp_x, tmp_y)
cnt=0
for i in range(n):
    for j in range(m):
        if list[i][j]=='0':
            list[i][j]='1'
            dfs(j, i)
            cnt+=1
print(cnt)
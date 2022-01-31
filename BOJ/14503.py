import sys
input=sys.stdin.readline

n, m=map(int, input().split())
r, c, d=map(int, input().split())

room=[]
for _ in range(n):
    room.append(list(map(int, input().split())))

visited=[[0]*m for _ in range(n)]
visited[r][c]=1
cnt=1

#북, 동, 남, 서
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

while True:
    flag=0
    for i in range(4):
        d-=1
        if d<0:
            d=3
        tmp_x=r+dx[d]
        tmp_y=c+dy[d]
        if visited[tmp_x][tmp_y]==0 and room[tmp_x][tmp_y]==0:
            r, c=tmp_x, tmp_y
            visited[tmp_x][tmp_y]=1
            flag=1
            cnt+=1
            break
    #네면이 모두 벽이거나 청소된 경우(flag=0)    
    if flag==0:
        tmp_x=r-dx[d]
        tmp_y=c-dy[d]
        
        #후진할 곳이 벽인 경우
        if room[tmp_x][tmp_y]==1:
            break

        r, c=tmp_x, tmp_y

print(cnt)
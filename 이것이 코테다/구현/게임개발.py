n, m=map(int, input().split())
a, b, direction=map(int, input().split())
matrix=[list(map(int, input().split())) for _ in range(n)]

dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
cnt=1
dir_cnt=0
while True:

    matrix[a][b]=-1 #가본칸

    if direction==0:
        direction=3
    else:
        direction-=1
    
    tmp_x=b+dx[direction]
    tmp_y=a+dy[direction]
    if matrix[tmp_y][tmp_x]==0:
        a=tmp_y
        b=tmp_x
        cnt+=1
        dir_cnt=0
    else:
        dir_cnt+=1

    if dir_cnt==4:
        tmp_x=b-dx[direction]
        tmp_y=a-dy[direction]
        if matrix[tmp_y][tmp_x]==1:
            break
        else:
            b=tmp_x
            a=tmp_y
            dir_cnt=0
print(cnt)
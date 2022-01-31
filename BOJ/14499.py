import sys
input=sys.stdin.readline

n, m, x, y, k=map(int, input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int, input().split())))

order=list(map(int, input().split()))

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]
t1, t2, t3, t4, t5, t6=0, 0, 0, 0, 0, 0

for i in range(k):
    tmp_x=x+dx[order[i]-1]
    tmp_y=y+dy[order[i]-1]
    if 0<=tmp_x<n and 0<=tmp_y<m:
        if order[i]==1:
            t2, t3, t4, t6= t3, t6, t2, t4
        elif order[i]==2:
            t2, t3, t4, t6 = t4, t2, t6, t3
        elif order[i]==3:
            t1, t2, t5, t6 = t6, t1, t2, t5
        else:
            t1, t2, t5, t6 = t2, t5, t6, t1

        if matrix[tmp_x][tmp_y]==0:
                matrix[tmp_x][tmp_y]=t2
        else:
            t2= matrix[tmp_x][tmp_y]
            matrix[tmp_x][tmp_y]=0
            
        x, y=tmp_x, tmp_y
        print(t6)

import sys
input=sys.stdin.readline

dx=[[0, 0, 0, 0], [0, 1, 2, 3], [0, 1, 0, 1], [0, 0, 0, 1], [0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 1, 1], [0, 1, 1, 2], [0, 0, 0, 1], [0, 1, 2, 1], [0, 0, 1, 1], [0, 1, 1, 2], [0, 1, 1, 1], [0, 0, 1, 2], [0, 0, 0, 1], [0, 1, 2, 2], [0, 1, 1, 2], [0, 0, 1, 1]]
dy=[[0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 2, 2], [0, 0, 0, 1], [0, 0, 1, 2], [0, 0, 0, -1], [0, -1, 0, 1], [0, 0, -1, 0], [0, 1, 2, 1], [0, 0, 0, 1], [0, 1, 1, 2], [0, 0, -1, -1], [0, 0, -1, -2], [0, 1, 1, 1], [0, 1, 2, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, -1, -1, -2]]

n, m=map(int, input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int, input().split())))

max=0
for i in range(n):
    for j in range(m):
        for k in range(19):
            sum=0
            flag=0
            for l in range(4):
                tmp_x=j+dx[k][l]
                tmp_y=i+dy[k][l]
                if 0<=tmp_x<m and 0<=tmp_y<n:
                    sum+=matrix[tmp_y][tmp_x]
                else:
                    flag=1
                    break
            if flag==0:
                if max==0 or max<sum:
                    max=sum
print(max)
import sys
input=sys.stdin.readline

n, m=map(int, input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i==0:
            continue
        
        matrix[i][j]+=matrix[i-1][j]

for i in range(m):
    x1, y1, x2, y2=map(int ,input().split())
    result=0
    for j in range(y1, y2+1):
        if x1!=1:
            result+=(matrix[x2-1][j-1]-matrix[x1-2][j-1])
        else:
            result+=(matrix[x2-1][j-1])
    print(result)
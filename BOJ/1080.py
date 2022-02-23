import sys
input=sys.stdin.readline

n, m=map(int, input().split())
matrix1=[]
matrix2=[]
for _ in range(n):
    matrix1.append(list(input().strip()))

for _ in range(n):
    matrix2.append(list(input().strip()))

def reverse(i, j):
    for a in range(i, i+3):
        for b in range(j, j+3):
            if matrix1[a][b]=='1':
                matrix1[a][b]='0'
            else:
                matrix1[a][b]='1'
cnt=0
for i in range(n-2):
    for j in range(m-2):
        if matrix1[i][j]!=matrix2[i][j]:
            reverse(i, j)
            cnt+=1

flag=0
for i in range(n):
    for j in range(m):
        if matrix1[i][j]!=matrix2[i][j]:
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print(-1)
else:
    print(cnt)
import sys
input=sys.stdin.readline

n=int(input())

matrix=[]
for i in range(n):
    matrix.append([])
    x, y=map(int, input().split())
    matrix[i].append(x)
    matrix[i].append(y)

matrix.sort()

for i in range(n):
    print(matrix[i][0], matrix[i][1])
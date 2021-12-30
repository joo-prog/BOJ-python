n, m=map(int, input().split())
matrix=[]
max_num=0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    max_num=max(min(matrix[i]), max_num)
print(max_num)
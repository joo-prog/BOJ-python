str1=input().strip()
str2=input().strip()
matrix=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1]==str2[j-1]:
            matrix[i][j]=matrix[i-1][j-1]+1
        else:
            matrix[i][j]=max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])
import sys
input=sys.stdin.readline

n=int(input())
tri=[]
for i in range(n):
    tri.append(list(map(int, input().split())))
    
    if i!=0:
        for j in range(len(tri[i])):
            if j==0:
                tri[i][j]+=tri[i-1][j]
            elif j==len(tri[i])-1:
                tri[i][j]+=tri[i-1][j-1]
            else:
                tri[i][j]+=max(tri[i-1][j], tri[i-1][j-1])

print(max(tri[n-1]))
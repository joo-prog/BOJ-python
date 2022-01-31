import sys
import itertools
input=sys.stdin.readline

n, m=map(int, input().split())
city=[]
house=[]
chicken=[]
min_len=-1

for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j]==1:
            house.append([i, j])
        elif city[i][j]==2:
            chicken.append([i, j])

result=list(itertools.combinations(chicken, m))
for i in range(len(result)):
    sum=0
    for x, y in house:
        tmp=-1
        for j in range(m):
            if tmp==-1:
                tmp=abs(x-result[i][j][0])+abs(y-result[i][j][1])
            else:
                tmp=min(tmp, abs(x-result[i][j][0])+abs(y-result[i][j][1]))
        sum+=tmp
    
    if min_len==-1 or min_len>sum:
        min_len=sum

print(min_len)

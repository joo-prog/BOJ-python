import sys
input=sys.stdin.readline

n=int(input())
wine=[]
tmp=0
for i in range(n):
    wine.append(int(input()))

dp_wine=[0]*n
dp_wine[0]=wine[0]
if n>=2:
    dp_wine[1]=wine[0]+wine[1]
    if n>=3:
        dp_wine[1]=wine[0]+wine[1]
        dp_wine[2]=max(dp_wine[1], wine[2]+wine[0], wine[1]+wine[2])
        for i in range(3, n):
            dp_wine[i]=max(wine[i]+wine[i-1]+dp_wine[i-3], wine[i]+dp_wine[i-2], dp_wine[i-1])

print(dp_wine[n-1])
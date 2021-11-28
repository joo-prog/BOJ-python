import sys
input=sys.stdin.readline

n, m=map(int, input().split())
li=[]
for _ in range(n):
    li.append(int(input()))

cnt=0
s=1
e=max(li)

while s<=e:
    cnt=0
    mid=(s+e)//2
    for item in li:
        cnt+=(item//mid)
    if cnt>=m:
        s=mid+1
    else:
        e=mid-1
print(e)
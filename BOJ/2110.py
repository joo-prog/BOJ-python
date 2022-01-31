import sys
input=sys.stdin.readline

n, c=map(int, input().split())
house=[]
for _ in range(n):
    house.append(int(input()))

house.sort()

start=1
end=house[-1]-house[0]
res=0

while start<=end:
    mid=(start+end)//2
    tmp=house[0]
    cnt=1

    for i in range(1, n):
        if house[i]>=tmp+mid:
            tmp=house[i]
            cnt+=1
    if cnt>=c:
        start=mid+1
        res=mid
    else:
        end=mid-1
        
print(res)
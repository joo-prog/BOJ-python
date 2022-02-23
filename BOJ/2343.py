n, m=map(int, input().split())
lecture=list(map(int, input().split()))

left=max(lecture)
right=sum(lecture)

while left<=right:
    mid=(left+right)//2
    cnt=0
    tmp_sum=0
    for i in lecture:
        if tmp_sum+i>mid:
            tmp_sum=0
            cnt+=1
        tmp_sum+=i
    cnt+=1
    if cnt<=m:
        right=mid-1
    elif cnt>m:
        left=mid+1

print(left)
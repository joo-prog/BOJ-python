n, m=map(int, input().split())
tree=list(map(int, input().split()))
s=1
e=max(tree)

while s<=e:
    cnt=0
    mid=(s+e)//2
    for item in tree:
        if item-mid>0:
            cnt+=(item-mid)
    if cnt>=m:
        s=mid+1
    else:
        e=mid-1

print(e)
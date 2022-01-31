n=int(input())
li=list(map(int, input().split()))

li.sort()
start=0
end=len(li)-1

while start<=end:
    mid=(start+end)//2
    if li[mid]==mid:
        print(mid)
        exit()
    elif li[mid]<mid:
        start=mid+1
    else:
        end=mid-1

print(-1)
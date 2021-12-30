n=int(input())
li=list(map(int, input().split()))
li.sort(reverse=True)

index=0
cnt=0
while index<n:
    if li[index]-1<=len(li[index+1:]):
        cnt+=1
        index+=li[index]
print(cnt)

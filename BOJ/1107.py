n=int(input())
m=int(input())
broken=[0]*10
if m!=0:
    li=list(map(int, input().split()))
    for i in li:
        broken[i]=1


if n>100:
    result=n-100
else:
    result=100-n

for i in range(1000001):
    flag=0
    for tmp in str(i):
        if broken[int(tmp)]==1:
            flag=1
            break
    if flag==0:
        result=min(result, len(str(i))+abs(i-n))

print(result)

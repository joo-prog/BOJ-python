import sys
input=sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

cnt=0
for i in range(n):
    flag=0
    if li[i]==1:
        continue
    else:
        for j in range(2, int(li[i]**(0.5))+1):
            if li[i]%j==0:
                flag=1
                break

        if flag==0:
            cnt+=1
print(cnt)

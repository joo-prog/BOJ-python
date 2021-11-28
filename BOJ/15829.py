n=int(input())

li=list(input().strip())
sum=0

for i in range(n):
    sum+=(ord(li[i])-ord('a')+1)*(31**i)

sum=sum%1234567891

print(sum)
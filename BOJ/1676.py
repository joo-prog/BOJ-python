n=int(input())

fac=1
for i in range(1, n+1):
    fac*=i

cnt=0
while fac!=0:
    tmp=fac%10
    fac=fac//10
    if tmp==0:
        cnt+=1
    else:
        break
    
print(cnt)
m, n=map(int,input().split())

for num in range(m, n+1):
    flag=0
    for j in range(2,int(num**0.5)+1):
        if (num%j==0):
            flag=1
            break
    if (flag==0)&(num!=1):
        print(num)
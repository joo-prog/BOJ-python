n=int(input())
tmp=n
for i in range(2, n+1):
    while tmp%i==0:
        print(i)
        tmp/=i
n=int(input())
tmp=2
if (n==1) | (n==2):
    print(n)
else:
    while(1):
        if tmp*2>=n:
            break
        tmp*=2
    
    print(2*(n-tmp))
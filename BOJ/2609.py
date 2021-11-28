n, m=map(int,input().split())

if n>m:
    min=m
    while (n%min!=0)|(m%min!=0):
        min-=1
    print(min)

    max=n
    while max%m!=0:
        max+=n
    print(max)
else:
    min=n
    while (n%min!=0)|(m%min!=0):
        min-=1
    print(min)
    
    max=m
    while max%n!=0:
        max+=m
    print(max)


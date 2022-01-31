t=int(input())
def get_lcm(m, n):
    if m>n:
        lcm=m
        while True:
            if lcm%m==0 and lcm%n==0:
                break
            lcm+=m
    else:
        lcm=n
        while True:
            if lcm%m==0 and lcm%n==0:
                break
            lcm+=n
    return lcm

for _ in range(t):
    m, n, x, y=map(int, input().split())
    lcm=get_lcm(m, n)
    flag=0
    for i in range(lcm//m+1):
        if (m*i+x)%n==y:
            flag=1
            res=m*i+x
            break
        elif (m*i+x)%n==0:
            if n==y:
                flag=1
                res=m*i+x
                break
    if flag==0:
        print(-1)
    else:
        print(res)
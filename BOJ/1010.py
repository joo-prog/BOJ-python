T=int(input())
for _ in range(T):
    n, m=map(int, input().split())
    tmp1, tmp2=1, 1
    if n>m-n:
        n=m-n
    for i in range(n):
        tmp1*=m-i
        tmp2*=(i+1)
    print(tmp1//tmp2)
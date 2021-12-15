n, m=map(int, input().split())

def fac(end):
    result=1
    for i in range(m):
        result*=(end-i)
    return result

if m>n-m:
    m=n-m
    
print(fac(n)//(fac(m)))
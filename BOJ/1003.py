t=int(input())

def fibonacci(n):
    if n==0:
        zero[n], one[n]=1, 0
        return
    elif n==1:
        zero[n], one[n]=0, 1
        return

    if (zero[n-1]==0)&(one[n-1]==0):
        fibonacci(n-1)
    if (zero[n-2]==0)&(one[n-2]==0):
        fibonacci(n-2)

    zero[n]=zero[n-1]+zero[n-2]
    one[n]=one[n-1]+one[n-2]
    return

for _ in range(t):
    n=int(input())
    zero=[0]*(n+1)
    one=[0]*(n+1)
    fibonacci(n)
    print(zero[n], one[n])
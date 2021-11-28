import sys
input=sys.stdin.readline

t=int(input())

def dp(num):
    if (num==1)|(num==2):
        return num
    if num==3:
        return 4
    return dp(num-1)+dp(num-2)+dp(num-3)

for _ in range(t):
    n=int(input())
    print(dp(n))

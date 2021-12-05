import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    a, b=map(int, input().split())
    A, B= a, b
    while a!=0:
        b=b%a
        a, b= b, a
    print(A*B//b)
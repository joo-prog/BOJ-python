import sys
input=sys.stdin.readline

n, m=map(int, input().split())
s1=set()
s2=set()
for _ in range(n):
    s1.add(input().strip())
for _ in range(m):
    s2.add(input().strip())

result=list(s1&s2)
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])
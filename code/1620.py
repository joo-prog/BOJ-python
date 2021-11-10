import sys
input=sys.stdin.readline

n, m=map(int, input().split())
dic={}
dic2={}

for i in range(1, n+1):
    name=input().strip()
    dic[name]=i
    dic[i]=name

for _ in range(m):
    find=input().strip()
    if find.isnumeric():
        print(dic[int(find)])
    else:
        print(dic[find])
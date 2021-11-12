import sys
input=sys.stdin.readline

n, m=map(int, input().split())
dic={}
for _ in range(n):
    site, password=input().strip('\n').split(' ')
    dic[site]=password

for _ in range(m):
    find=input().strip('\n')
    print(dic[find])
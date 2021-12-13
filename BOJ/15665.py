from itertools import product

n, m=map(int, input().split())
li=sorted(list(map(int, input().split())))
s=sorted(list(set(product(li,repeat=m))))

for i in s:
    for j in i:
        print(j, end=' ')
    print()
from itertools import product

n, m=map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in product(li, repeat=m):
    for j in i:
        print(j, end=' ')
    print()
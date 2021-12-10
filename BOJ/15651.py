from itertools import product

n, m=map(int, input().split())
li=[i for i in range(1, n+1)]
for i in product(li, repeat=m):
    for j in i:
        print(j, end=' ')
    print()
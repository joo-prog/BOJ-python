from itertools import combinations_with_replacement

n, m=map(int, input().split())
li=[i for i in range(1, n+1)]
li.sort()
for i in combinations_with_replacement(li, m):
    for j in i:
        print(j, end=' ')
    print()
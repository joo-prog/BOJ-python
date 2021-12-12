from itertools import combinations

n, m=map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in combinations(li, m):
    for j in i:
        print(j, end=' ')
    print()
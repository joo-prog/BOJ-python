from itertools import permutations

n, m=map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in permutations(li, m):
    for j in i:
        print(j, end=' ')
    print()
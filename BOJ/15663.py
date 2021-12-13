from itertools import permutations

n, m=map(int, input().split())
li=sorted(list(map(int, input().split())))
s=sorted(list(set(permutations(li,m))))

for i in s:
    for j in i:
        print(j, end=' ')
    print()
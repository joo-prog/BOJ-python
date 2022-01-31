from itertools import combinations
n, m=map(int, input().split())
al=input().strip().split()
al.sort()
li=list(combinations(al, n))

tmp=['a', 'e', 'i', 'o', 'u']

for i in li:
    word=''
    cnt1=0
    cnt2=0
    for j in range(n): 
        word+=i[j]
        if i[j] in tmp:
            cnt1+=1
        else:
            cnt2+=1
    if cnt1>=1 and cnt2>=2:
        print(word)
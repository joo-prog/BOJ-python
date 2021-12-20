n=int(input())
tmp_n=n
result=0
cnt=0
tree=64
while True:
    if n==result:
        break
    if tree>tmp_n:
        tree=tree//2
    else:
        tmp_n-=tree
        result+=tree
        tree=tree//2
        cnt+=1
print(cnt)
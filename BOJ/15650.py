n, m=map(int, input().split())

d=[]
for i in range(m):
    d.append(i+1)

while True:
    for i in range(m):
        print(d[i], end=' ')
    print()
    tmp_index=-2
    if d[-1]!=n:
        d[-1]+=1
    else:
        if d[0]==n-m+1 and d[-1]==n:
            break
        
        while d[tmp_index]==d[tmp_index+1]-1:
            tmp_index-=1

        d[tmp_index]+=1
        for i in range(tmp_index+1, 0):
            d[i]=d[i-1]+1
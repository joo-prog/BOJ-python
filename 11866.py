n, k=map(int, input().split())

li=[item for item in range(1, n+1)]
index=-1+k

print('<', end='')
while len(li)!=0:
    index=index%len(li)
    if len(li)!=1:
        print('%d,'%li[index], end=' ')
    else:
        print('%d>'%li[index])
    del li[index]
    index+=k-1
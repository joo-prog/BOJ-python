n=int(input())
order=list(input().split())
x, y=1,1
for i in order:
    if i=='L':
        if x!=1:
            x-=1
    elif i=='R':
        if x!=n:
            x+=1
    elif i=='U':
        if y!=1:
            y-=1
    else:
        if y!=n:
            y+=1
print(y, x)
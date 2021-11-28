s=input().split('-')
li=[]
for i in s:
    sum=0
    tmp=i.split('+')
    for j in tmp:
        sum+=int(j)
    li.append(sum)
for i in range(1, len(li)):
    li[0]-=li[i]
print(li[0])
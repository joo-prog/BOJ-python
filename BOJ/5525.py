n=int(input())
m=int(input())
string=input().strip()

cnt=0
i=0
pattern=0
while i<m-2:
    if string[i]=='I' and string[i+1]=='O' and string[i+2]=='I':
        pattern+=1
        if pattern==n:
            cnt+=1
            pattern-=1
        i+=2
    else:
        pattern=0
        i+=1
print(cnt)
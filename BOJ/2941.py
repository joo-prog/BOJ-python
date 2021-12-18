string=input().strip()
cnt=0
i=0

while i!=len(string):
    flag=0
    if string[i]=='c':
        if i+1<len(string):
            if string[i+1]=='=' or string[i+1]=='-':
                i+=2
                cnt+=1
                flag=1
    elif string[i]=='d':
        if i+2<len(string) and string[i+1:i+3]=='z=':
            i+=3
            cnt+=1
            flag=1
        elif i+1<len(string) and string[i+1]=='-':
            i+=2
            cnt+=1
            flag=1
    elif i+1< len(string) and (string[i:i+2]=='lj' or string[i:i+2]=='nj' or string[i:i+2]=='s=' or string[i:i+2]=='z='):
        i+=2
        cnt+=1
        flag=1
    if flag==0:
        i+=1
        cnt+=1
        
print(cnt)
n=int(input())

for i in range(n):
    vps=0
    tmp_li=input()
    for item in tmp_li:
        if item=='(':
            vps+=1
        else:
            vps-=1

        if vps<0:
            break
        
    if vps==0:
        print('YES')
    else:
        print('NO')
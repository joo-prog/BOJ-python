import sys
input=sys.stdin.readline

n, m=map(int, input().split())

matrix=[]
for i in range(n):
    matrix.append(input().strip())

cnt=64
for i in range(0, n-7):
    for j in range(0, m-7):
        cnt_1=0
        cnt_2=0
        for k in range(0,8):
            for l in range(0, 8):
                if k%2==0:
                    if l%2==0:
                        if matrix[i+k][j+l]=='B':
                            cnt_1+=1
                        else:
                            cnt_2+=1
                    else:
                        if matrix[i+k][j+l]=='W':
                            cnt_1+=1
                        else:
                            cnt_2+=1
                else:
                    if l%2==0:
                        if matrix[i+k][j+l]=='W':
                            cnt_1+=1
                        else:
                            cnt_2+=1
                    else:
                        if matrix[i+k][j+l]=='B':
                            cnt_1+=1
                        else:
                            cnt_2+=1
        if cnt_1>cnt_2:
            if cnt_2<cnt:
                cnt=cnt_2
        else:
            if cnt_1<cnt:
                cnt=cnt_1
        
        if cnt==0:
            break
    if cnt==0:
        break

print(cnt)
num=int(input())

matrix=[]
for _ in range(num):
    matrix.append(list(map(int, input().split())))

def white_blue(n, row, col):
    if n==2:
        tmp=matrix[row][col]+ matrix[row+1][col]+matrix[row+1][col+1]+matrix[row][col+1]
        if tmp==4:
            return 1, 0, 1
        elif tmp==0:
            return 0, 1, 0
        else:
            return tmp, 4-tmp, 5

    tmp_b1, tmp_w1, flag_1=white_blue(n//2, row, col)
    tmp_b2, tmp_w2, flag_2=white_blue(n//2, row, col+(n//2))
    tmp_b3, tmp_w3, flag_3=white_blue(n//2, row+(n//2), col)
    tmp_b4, tmp_w4, flag_4=white_blue(n//2, row+(n//2), col+(n//2))

    tmp_w=tmp_w1+tmp_w2+tmp_w3+tmp_w4
    tmp_b=tmp_b1+tmp_b2+tmp_b3+tmp_b4
    flag=flag_1+flag_2+flag_3+flag_4

    if flag==4:
        return 1, 0, 1
    elif flag==0:
        return 0 ,1, 0
    else:
        return tmp_b, tmp_w, 5
    
blue, white, _=white_blue(num,0,0,)

print(white)
print(blue)

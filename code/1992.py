import sys
input=sys.stdin.readline

n=int(input())

image=[]
for _ in range(n):
    image.append(list(map(int, input().strip())))

def zip(num, row, col):
    if num==1:
        return image[row][col], image[row][col]
    flag=0
    tmp=num//2
    li=[]
    a, flag1=zip(tmp, row, col)
    b, flag2=zip(tmp, row, col+tmp)
    c, flag3=zip(tmp, row+tmp, col)
    d, flag4=zip(tmp, row+tmp, col+tmp)

    li.extend([a, b, c, d])
    flag=flag1+flag2+flag3+flag4

    if flag==0:
        return a, 0
    elif flag==4:
        return a, 1
    else:
        return tuple(li), 5

zip_image, _ = zip(n,0,0)
print(str(zip_image).replace(', ', ""))
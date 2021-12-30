s=input().strip()
index=0
cnt_zero=0
cnt_one=0

while True:
    if index>=len(s):
        break
    if s[index]=='0':
        while s[index]=='0':
            index+=1
            if index>=len(s):
                break
        cnt_zero+=1
    else:
        while s[index]=='1':
            index+=1
            if index>=len(s):
                break
        cnt_one+=1
print(min(cnt_zero, cnt_one))
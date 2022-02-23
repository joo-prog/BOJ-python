n=int(input())
s=['*']

def even(s):
    tmp=[]
    c=len(s)
    tmp.append('*'*(4*c+1))
    for i in range(1, c+1):
        tmp.append(' '*i+'*'+' '*(c-i)+s[i-1]+' '*2*(c-i)+'*')
    for i in range(1, c):
        tmp.append(' '*(c+i)+'*'+' '*(2*c-1-2*i)+'*')
    tmp.append(' '*2*c+'*')
    return tmp

def odd(s):
    tmp=[]
    c=len(s)
    tmp.append(' '*2*c+'*')
    for i in range(1, c):
        tmp.append(' '*(2*c-i)+'*'+' '*(2*i-1)+'*')
    for i in range(1, c+1):
        tmp.append(' '*(c+1-i)+'*'+' '*(i-1)+s[i-1]+' '*2*(i-1)+'*')
    tmp.append('*'*(4*c+1))
    return tmp

for i in range(2, n+1):
    if i%2==0:
        s=even(s)
    else:
        s=odd(s)

for i in range(len(s)):
    print(s[i])
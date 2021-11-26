from collections import deque
li=list(input().strip())

q=deque()
for i in li:
    if 'A'<=i<='Z':
        print(i, end='')
    else:
        if i==')':
            while True:
                p=q.pop()
                if p=='(' or len(q)==0:
                    break
                print(p, end='')
        elif i=='*' or i=='/':
            while q:
                if len(q)==0 or q[-1]=='+' or q[-1]=='-' or q[-1]=='(':
                    break
                p=q.pop()
                print(p, end='')
            q.append(i)
        elif i=='(':
            q.append(i)
        else:
            if q:
                while True:
                    if len(q)==0 or q[-1]=='(':
                        break
                    p=q.pop()
                    print(p, end='')
            q.append(i)

while q:
    p=q.pop()
    if p!=')' and p!='(':
        print(p, end='')
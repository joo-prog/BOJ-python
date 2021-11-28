import sys
input=sys.stdin.readline

while True:
    deque=[]
    number=int(input())
    if (number==0):
        break
    
    while number!=0:
        deque.append(number%10)
        number=number//10
        
    flag=1
    while len(deque)>1:
        if deque.pop(0)!=deque.pop():
            flag=2
            print('no')
            break
    
    if flag==1:
        print('yes')
    
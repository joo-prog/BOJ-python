n=int(input())
k=0
while 3**k!=n:
    k+=1

s=['***','* *', '***']
def rec(a):
    for i in range(3**a):
        s.append(s[i])
        s[i]=s[i]*3
    for i in range(3**a, 2*3**a):
        s.append(s[i])
        s[i]=s[i]+' '*(3**a)+s[i]
    for i in range(2*3**a, 3*3**a):
        s[i]=s[i]*3

for i in range(1, k):
    rec(i)
for i in range(n):
    print(s[i])
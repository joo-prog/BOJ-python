n=int(input())
k=0
while n!=3*(2**k):
    k+=1

s=['  *   ', ' * *  ', '***** ']

def star(shift):
    c=len(s)
    for i in range(c):
        s.append(s[i]+s[i])
        s[i]=('   '*shift+s[i]+'   '*shift)

for i in range(k):
    star(2**i)
for i in range(n):
    print(s[i])
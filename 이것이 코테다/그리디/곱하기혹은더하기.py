n=input()

for i in range(0, len(n)):
    if i==0:
        result=int(n[i])
    else:
        result=max(result+int(n[i]), result*int(n[i]))
print(result)
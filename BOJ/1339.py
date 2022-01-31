n=int(input())
word=[]
max_num=9
for _ in range(n):
    word.append(input().strip())

dic={}
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in dic:
            dic[word[i][j]]+=10**(len(word[i])-1-j)
        else:
            dic[word[i][j]]=10**(len(word[i])-1-j)

res=[]
for value in dic.values():
    res.append(value)
res.sort(reverse=True)

sum=0
for i in res:
    sum+=(max_num*i)
    max_num-=1
print(sum) 
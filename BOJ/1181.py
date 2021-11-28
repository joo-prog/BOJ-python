import sys
input=sys.stdin.readline

n=int(input())

word_list=[]
for i in range(n):
    word=input().strip()
    word_list.append([word,len(word)])

word_list.sort(key=lambda x:[x[1],x[0]])

for i in range(n):
    if i==0:
        print(word_list[i][0])
    elif word_list[i][0]!=word_list[i-1][0]:
        print(word_list[i][0])

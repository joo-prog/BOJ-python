num=int(input())
num_list=[]
while num!=0:
    num_list.append(num%10)
    num=num//10
num_list.sort(reverse=True)
for i in num_list:
    print(i, end='')
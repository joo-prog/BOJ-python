def solution(record):
    answer = []
    dic={}

    for i in range(len(record)):
        li=record[i].split()
        if li[0]=='Enter':
            if li[1] not in dic.keys():
                dic[li[1]]=li[2]
            else:
                dic[li[1]]=li[2]
        elif li[0]=='Change':
            dic[li[1]]=li[2]

    for i in range(len(record)):
        li=record[i].split()
        if li[0]=='Enter':
            answer.append(dic[li[1]]+'님이 들어왔습니다.')
        elif li[0]=='Leave':
            answer.append(dic[li[1]]+'님이 나갔습니다.')

    return answer
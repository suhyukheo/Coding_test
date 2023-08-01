def solution(ingredient):
    answer = 0
    cnt = 0
    while cnt < len(ingredient)-3:
        if ingredient[cnt:cnt+4] == [1,2,3,1]:
            answer +=1
            del ingredient[cnt:cnt+4]
            if cnt < 4:
                cnt = 0
            else:
                cnt -= 3
        else:
            cnt += 1      

    return answer

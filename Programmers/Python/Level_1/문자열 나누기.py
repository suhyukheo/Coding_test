def solution(s):
    answer = 0
    x = s[0]
    x_cnt,a_cnt = 0,0
    
    for i in s:
        if x_cnt != 0 and x_cnt == a_cnt:
            x_cnt,a_cnt = 0,0
            answer +=1
            x=i
        if x == i:
            x_cnt +=1
        else:
            a_cnt +=1

    return answer+1

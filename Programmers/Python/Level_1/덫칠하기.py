def solution(n, m, section):
    answer = 0
    pointer = 0
    for i in section:
        if i > pointer:
            answer +=1
            pointer = (i+m)-1
    return answer

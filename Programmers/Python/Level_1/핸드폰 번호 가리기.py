def solution(phone_number):
    answer=list(phone_number)
    answer[0:len(answer)-4]='*'*(len(answer)-4)
    answer="".join(answer)
    return answer
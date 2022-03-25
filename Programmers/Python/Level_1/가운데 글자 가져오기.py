def solution(s):
    answer=[]
    mid=len(s)//2
    if len(s)%2==1:
        answer.append(s[mid])
    else:
        answer.append(s[mid-1:mid+1])
    return "".join(answer) # 기본형 "구분자".join(리스트)

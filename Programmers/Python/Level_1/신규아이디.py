def solution(new_id):
    new_id=new_id.lower()# 1단계
    answer=""
    for i in new_id:
        if i=="-" or i=="_" or i=="." or i.isdigit() or i.isalpha():# 2단계
            answer+=i
            
    while '..' in answer : # 3단계
        answer = answer.replace('..','.')
        
    answer=list(answer)
    
    if answer[0] == '.': # 4단계
            answer.pop(0)
    elif answer[-1] == '.':
            answer.pop(-1)
    answer = "".join(answer)
    
    # 5단계
    if len(answer)==0:
        answer+="a"
    #6단계
    if len(answer)>=16:
        answer=answer[0:15]
    if answer[-1]==".":
        answer=answer[:-1]
    #7단계
    while len(answer)<=2:
        answer+=answer[-1]
    
        
    return answer

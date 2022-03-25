def solution(progresses, speeds):
    answer = []
    result=[]
    for pro,spd in zip(progresses,speeds):
        re_=100-pro
        if re_%spd==0:
            answer.append(re_//spd)
        else:
            answer.append((re_//spd)+1)
    max_=answer[0]
    cnt=0
    for i in answer:
        if max_<i:
            max_=i
            result.append(cnt)
            cnt=1
        else:
            cnt+=1
    result.append(cnt)
    return result

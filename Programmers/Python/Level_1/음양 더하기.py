def solution(numbers):
    answer=0
    result=[0]*10
    for i in numbers:
        if result[i]==0:
            result[i]+=1
    for i in range(len(result)):
        if result[i]==0:
            answer+=i
    return answer
from itertools import combinations
def solution(numbers):
    
    answer=[]
    arr=list(combinations(numbers,2))
    for i in arr:
        answer.append(sum(i))
    answer=list(set(answer))
    answer.sort()   
    
    return answer
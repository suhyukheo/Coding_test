def solution(num):
    answer=0
    while True:
        if answer==500:
            return -1   
        elif num==1:
            return answer
        if num%2==0:
            num=num/2
            answer+=1   
        else:
            num=(num*3)+1
            answer+=1
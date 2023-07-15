def GetDivisor(number):
    answer = []
    for i in range(1, int(number**(1/2)) + 1):
        if (number % i == 0):
            answer.append(i) 
            if ( (i**2) != number): 
                answer.append(number//i)
    return len(answer)

def solution(number, limit, power):
    result = [1]
    for i in range(2,number+1):
        Div = GetDivisor(i)
        if Div > limit:
            result.append(power)
        else:
            result.append(Div)
    return sum(result)

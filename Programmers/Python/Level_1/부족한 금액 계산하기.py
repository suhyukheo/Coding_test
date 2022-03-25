def solution(price, money, count):
    result=0
    for i in range(count):
        result=price*(i+1)
        money-=result
    if money<0:
        return -(money)
    else:
        return 0
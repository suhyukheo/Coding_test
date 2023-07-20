def solution(n):
    fibo = [1]*(n+1)
    if n > 2:
        for i in range(2,n+1):
            fibo[i] = fibo[i-1]%1234567 + fibo[i-2]%1234567
        return fibo[-1]%1234567
    else: 
        return n

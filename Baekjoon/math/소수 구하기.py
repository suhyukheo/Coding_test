def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return sieve
                
p_list=prime_list(1000001)
a,b =input("").split(" ")
cnt = 0 
for i in range(int(a),int(b)):
   if p_list[i] == True:
     print(i)

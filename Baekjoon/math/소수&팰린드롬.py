def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return sieve
  
prime = prime_list(1100000)
n = int(input())

for i in range(n,len(prime)):
  if n == 1:
    print(2)
    break
  if prime[i] == True:
    a = str(i)
    half = len(a)//2
    if len(a)%2 == 0:
      reversed_str = "".join(reversed(a[half:len(a)]))
      if a[:half] == reversed_str:
        print(i)
        break
    else:
      reversed_str = "".join(reversed(a[half+1:len(a)]))
      if a[:half] == reversed_str:
        print(i)
        break

n=1000
sieve = [True] * n
prime=[]
cnt=0
for i in range(2, n):
  if sieve[i] == True:
    prime.append(i)
    for j in range(i+i,n,i): # i이후 i의 배수들을 False 판정
          sieve[j] = False
          
N=int(input())
nums=list(map(int,input().split()))
for i in range(N):
  if nums[i] in prime:
    cnt+=1
print(cnt)
  
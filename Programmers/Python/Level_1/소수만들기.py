from itertools import combinations
nums=[1,2,3,4]
count=0
result=[]
n=0
nums.sort(reverse=True)
for i in range(3):
    n+=nums[i]
    
nums=list(combinations(nums,3))

sieve=[True]*(n+1)
print(sieve)
m=int(n**0.5)
for i in range(2,m+1):
    if sieve[i]==True:
        for j in range(i+i,n+1,i):
            sieve[j]=False
for i in range(len(sieve)):
    if sieve[i]==True :
        result.append(i)                 
for i in nums:
    if sum(i) in result:
        print(sum(i))
        count+=1
print(sieve)    

print(count)
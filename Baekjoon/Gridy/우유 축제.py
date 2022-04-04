milk_n=0
count=0
n=int(input())
milk_store=list(map(int,input().split()))
for i in range(n):
  if milk_n==milk_store[i]:
    milk_n+=1
    count+=1
    if milk_n==3:
      milk_n=0
print(count)

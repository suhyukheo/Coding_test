a,b=map(int,input().split(" "))
result=[]
num=0
for i in range(1,b+1):#0일때
  if num>=b:
    break
  c=i
  for j in range(i):
    if num>=b:
     break
    num+=1
    result.append(c)
num=0
for i in range(a-1,b):
  num+=result[i]
print(num)

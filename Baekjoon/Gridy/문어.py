N=int(input())
result=[]
if N%2==0: [result.append(2) if i%2==0 else result.append(1) for i in range(1,N+1)]
elif N%2!=0:
  [result.append(2) if i%2==0 else result.append(1) for i in range(1,N)]
  result.append(3)
for i in result:
  print(i,end=" ")
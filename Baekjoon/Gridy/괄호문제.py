n=int(input())
for i in range(n):
  cnt=0
  result=input()
  for j in result:
    if cnt==-1:
      break
    if j=='(':
      cnt+=1
    else:
      cnt-=1
  if cnt==0:
    print('Yes')
  else:
    print('No')
      
  
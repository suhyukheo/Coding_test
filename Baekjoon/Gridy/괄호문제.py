# n=int(input())
# for i in range(n):
#   cnt=0
#   result=input()
#   for j in result:
#     if cnt==-1:
#       break
#     if j=='(':
#       cnt+=1
#     else:
#       cnt-=1
#   if cnt==0:
#     print('Yes')
#   else:
#     print('No')
  
from collections import deque
n=int(input())
que=deque()
for i in range(n):
  que.clear()
  a=list(input())
  for i in range(len(a)):
    if len(que)==0:
      que.append(a[i])
    elif len(que)>=1:
      if a[i]==')':
        que.pop()
        print(a)
      else:
        que.append(a[i])


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
#     print('YES')
#   else:
#     print('NO')
  
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
      q=que.pop()
      if a[i] == ')' and q == '(':
        continue
      else:
        que.append(q)
        que.append(a[i])
  if len(que)==0:
    print('YES')
  else:
    print('NO')


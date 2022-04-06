stack=[]
result=[]
n=int(input())
for i in range(n):
  a=list(map(str,input().split(" ")))
  if a[0]=="push":
    stack.append(a[1])
    continue
  elif a[0]=="pop":
    if len(stack)>0:
      result.append(stack.pop())
      continue
    else:
      result.append(-1)
      continue
  elif a[0]=="size":
    result.append(len(stack))
    continue
  elif a[0]=="empty":
    if len(stack)==0:
      result.append(1)
    else:
      result.append(0)
    continue
  elif a[0]=="top":
    if len(stack)==0:
      result.append(-1)
    else:
      result.append(stack[-1])
  a.clear()
    
for i in range(len(result)):
  print(result[i])
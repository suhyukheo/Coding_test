total=0
n=input()
n=sorted(n, reverse=True)
if '0' not in n:
  print(-1)
else:
  for i in n:
    total+=int(i)
  if total%3!=0:
    print(-1)
  else:
    print("".join(n))
    

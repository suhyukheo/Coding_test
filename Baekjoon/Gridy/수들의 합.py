n=int(input())
i=0
total=0
while True:
  if total==n:
    print(i)
    break
  elif total>n:
    print(i-1)
    break
  i+=1
  total+=i
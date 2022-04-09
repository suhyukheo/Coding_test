result=[]
n=int(input())
for i in range(n):
  sum_=0
  cnt=0
  quiz=list(input())
  for i in quiz:
    if i =="O":
      cnt+=1
      sum_+=cnt
    elif i =="X":
      cnt=0
  result.append(sum_)
for i in result:
  print(i)
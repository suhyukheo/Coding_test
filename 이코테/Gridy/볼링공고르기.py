from itertools import combinations
n,m=map(int,input().split(" "))
ball=list(map(int,input().split(" ")))
result = list(combinations(ball,2))
for i in result:
  if i[0]==i[1]:
    result.remove(i)
print(len(result))

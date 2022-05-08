n=list(map(int,input().split(" ")))
a=0
target=1
n.sort()
for date in n:
  if target<date:
    break
  target+=date
print(target)
print(a)
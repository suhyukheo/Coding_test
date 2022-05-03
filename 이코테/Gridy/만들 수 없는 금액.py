n=list(map(int,input().split(" ")))
target=1
n.sort()
for date in n:
  if target<date:
    break
  target+=date
print(target)
n = list(map(int,list(input().split(" "))))
frute = list(map(int,list(input().split(" "))))
frute.sort()
for i in frute:
  if n[1] >= i:
    n[1] +=1
print(n[1])

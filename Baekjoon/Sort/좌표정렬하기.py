n = int(input())
ret = []
for i in range(n):
  a = list(map(int,list(input("").split(" "))))
  ret.append(a)
ret.sort(key = lambda x:(x[1],x[0]))
for i in ret:
  print(str(i[0])+' '+str(i[1]))

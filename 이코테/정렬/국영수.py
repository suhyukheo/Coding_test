n=int(input())
std=[]
for i in range(n):
  std.append(input().split(" "))
std.sort(key=lambda x:-int((x[1]), int(x[2]),-int(x[3])))
print(std)
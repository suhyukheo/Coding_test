import sys
new_set = set()
n = int(sys.stdin.readline())
for i in range(n):
  a = list(sys.stdin.readline().rstrip().split(" "))
  if len(a) >= 2:
    if a[0] == "add":
      new_set.add(a[1])
    elif a[0] == "remove":
      if a[1] in new_set:new_set.remove(a[1])
    elif a[0] == "toggle":
      if a[1] in new_set :
        new_set.remove(a[1])
      else:
        new_set.add(a[1])
    elif a[0] == "check":
      if a[1] in new_set:
        print("1")
      else:
        print("0")
  else:
    if a[0] == "all":
      new_set = set()
      new_set.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif a[0] == "empty":
      new_set.clear()

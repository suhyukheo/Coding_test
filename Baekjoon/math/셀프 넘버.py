n_list = [False]*10001
answer = []

for i in range(1,10001):
  j = list(str(i))
  a = sum(list(map(int,j)))
  try:
    n_list[a+i] = True
  except:
    continue
    
for i in range(1,len(n_list)):
  if n_list[i] == False:
    print(i)

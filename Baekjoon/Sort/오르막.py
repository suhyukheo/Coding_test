n = list(map(int,input(" ").split(" ")))
chk = n[0]
answer = "Good"
if len(n) < 2:
  print(answer)
else:
  for i in range(1,len(n)):
    if chk > n[i]:
      answer = "Bad"
      break
    else:
      chk = n[i]
  print(answer)
  

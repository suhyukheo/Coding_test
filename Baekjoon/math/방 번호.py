num_set = ["0","1","2","3","4","5","6","6","7","8"]
n = list(input("").replace("9","6"))
answer = 1
#remove함수는 한개만 제거 

while n:
  a = n.pop(0)
  if a in num_set:
    num_set.remove(a)
  else:
    n.append(a)
    for i in range(0,10):
      if i == 9:
        num_set.append(str(6))
      num_set.append(str(i))
    answer +=1
    
print(answer)

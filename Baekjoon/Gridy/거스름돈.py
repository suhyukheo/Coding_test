coins = [500,100,50,10,5,1]
n = int(input(""))
n = 1000-n
answer = 0
for i in coins:
  answer +=n//i
  n = n%i       
print(answer)

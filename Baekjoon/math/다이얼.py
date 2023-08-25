dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = input("")
answer = 0 
for i in alpha:
  for j in range(len(dial)):
    if i in dial[j]:
      answer +=(j+3)
      
print(answer)

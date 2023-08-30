alpha_dict = {}
for i in range(26):
  alpha_dict[chr(ord('A')+i)] = 0
  
a = input("").upper()

for i in a:
  alpha_dict[i] +=1

sorted_dict = sorted(alpha_dict.items(),key = lambda x:x[1],reverse=True)

if sorted_dict[0][1] == sorted_dict[1][1]:
  print("?")
else:
  print(sorted_dict[0][0])

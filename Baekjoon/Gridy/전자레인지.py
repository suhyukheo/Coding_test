T=int(input())
A_T=T%300
B_T=A_T%60
if T%10!=0:
  print(-1)
else:
 print(T//300,A_T//60,B_T//10)
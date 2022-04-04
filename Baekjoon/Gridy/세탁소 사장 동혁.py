Q,D,N,P=25,10,5,1
T=int(input())
C=[]
for i in range(T):
  C.append(int(input()))

for i in range(T):
  a=C[i]%Q
  b=a%D
  c=b%N
  print(C[i]//Q, a//D, b//N, c//P)
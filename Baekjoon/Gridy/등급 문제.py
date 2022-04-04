n,k=map(int,input().split())
arr=0
for i in range(k):
  a=int(input())
  arr+=a
print((arr-(3*(n-k)))/n,(arr+(3*(n-k)))/n)
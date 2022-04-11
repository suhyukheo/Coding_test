a=input()
zero=0
one=0
if a[0]=='0':
  zero=1
elif a[0]=='1':
  one=1
for i in range(1,len(a)):
  if a[i-1]!=a[i] and a[i]=='1':
    one+=1
  elif a[i-1]!=a[i] and a[i]=='0':
    zero+=1
print(min(zero,one))

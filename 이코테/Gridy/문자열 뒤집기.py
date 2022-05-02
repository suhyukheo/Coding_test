s=list(input())
zero=0
one=0
num=0
num=s[0]
if num=='0':
  zero+=1
elif num=='1':
  one+=1
for i in range(1,len(s)):
  if num!=s[i]:
    num=s[i]
    if s[i]=='1':
      one+=1
    elif s[i]=='0':
      zero+=1
print(min(one,zero))
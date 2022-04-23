a,b=map(int,input().split(" "))
if a<b:
  a,b=b,a
def GCD(a,b):
  if b==0: 
    return a
  else: 
    return GCD(b,a%b)
gcd=GCD(a,b)
print(gcd)
print(int((a*b)/gcd))
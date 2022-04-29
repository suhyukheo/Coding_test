result=[]

n=int(input())
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))

a.sort()
b.sort(reverse=True)

def mult(a,b):
  return a*b

for i in range(n):
  c=mult(a[i],b[i])
  result.append(c)
  
print(sum(result))

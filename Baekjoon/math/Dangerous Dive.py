a,b = map(int,list(input("").split(" ")))
c = list(map(int,list(input("").split(" "))))
n = [i for i in range(1,int(a)+1)]

for i in c:
    if i in n:
        n.remove(i)        
if len(n) == 0:
    print("*")
else:
    n = list(map(str,n))
    print(" ".join(n)) 

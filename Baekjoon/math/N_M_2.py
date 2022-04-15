n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for a in range(1,n+1):
     s.append(a) 
     for i in range(1,n+1):
       if i >s[-1]:
        s.append(i)
        dfs()
        s.pop()
 
dfs()
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
visted=[0]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)
  
def dfs(graph,node,visted):
  visted[node]=1
  for node in graph[node]:
    if visted[node]==0:
      dfs(graph,node,visted)
  return visted
  
print(sum(dfs(graph,1,visted))-1)
  
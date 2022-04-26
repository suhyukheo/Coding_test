n=int(input())
result=[]
array=[]
visited=[ [0]*n for _ in range(n)]
for i in range(n):
  a=list(map(int,input()))
  array.append(a)

cnt=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(array,x,y):
  visited[x][y]=1
  global cnt
  if array[x][y]==1:
    cnt+=1
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and ny>=0 and nx<n and ny<n:
      if array[nx][ny]==1 and visited[nx][ny]==0:
        dfs(array,nx,ny)
         

for i in range(n):
  for j in range(len(array[0])):
    if array[i][j]==1 and visited[i][j]==0:
      dfs(array,i,j)
      result.append(cnt)
      cnt=0
result.sort()
print(len(result))
for i in result:
  print(i) 
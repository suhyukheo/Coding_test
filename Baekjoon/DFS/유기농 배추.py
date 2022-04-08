import sys
sys.setrecursionlimit(10000)


t=int(input())
result=[]
for i in range(t):
  m,n,k=map(int,input().split(" "))
  cnt=0
  array=[[0]*n for i in range(m)]
  
  def dfs(array,x,y):
   dx=[-1,1,0,0]
   dy=[0,0,-1,1]
   for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and ny>=0 and nx<m and ny<n:
        if array[nx][ny]==1:
          array[nx][ny]=-1
          dfs(array,nx,ny)
   return True
  for i in range(k):
   a,b=map(int,sys.stdin.readline().strip().split(" "))
   array[a][b]=1
  
  for i in range(len(array)):
   for j in range(len(array[0])):
     if array[i][j]==1:
         dfs(array,i,j)
         cnt+=1
  result.append(cnt)

for i in range(len(result)):
  print(result[i])


      

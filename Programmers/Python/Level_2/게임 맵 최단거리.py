from collections import deque 
def solution(maps):
    n,m=len(maps),len(maps[0])
    q=deque([(0,0)])
    visted=[[0]*m for i in range(n)]
    visted[0][0]=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y=q.popleft()
        if x==n-1 and y==m-1:
            return maps[-1][-1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and ny<m and nx<n:
                if visted[nx][ny]==0 and maps[nx][ny]!=0:
                    maps[nx][ny]=maps[x][y]+1
                    q.append((nx,ny))
                    visted[nx][ny]=1
    return -1
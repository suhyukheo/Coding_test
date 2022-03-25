def solution(N, stages):
    
    count=[[i,0] for i in range(1,N+1)]
    result=[]
    n=len(stages)#스테이지 수
    for i in range(len(count)): 
        if n<=0:
            break
        for j in stages:
            if n<=0:
                break
            if count[i][0]==j:
                count[i][1]+=1
                n-=1
    n=len(stages)
    for i in range(len(count)):
        if n<=0:
            break
        a=count[i][1]
        count[i][1]=count[i][1]/n
        n-=a
    count=sorted(count,key=lambda x:-float(x[1]))
    for i in range(len(count)):
        result.append(count[i][0])
    
    return result
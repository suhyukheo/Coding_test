def solution(answer):
    giver1=[1,2,3,4,5]
    giver2=[2,1,2,3,2,4,2,5]
    giver3=[3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]
    result=[]
    
    for i in range(len(answer)):
        
        n1=i%len(giver1)
        if answer[i]==giver1[n1]:
            count[0]+=1
            
        n2=i%len(giver2)
        if answer[i]==giver2[n2]:
            count[1]+=1 
        
        n3=i%len(giver3)
        if answer[i]==giver3[n3]:
            count[2]+=1
    
    max_= max(count)
    
    for idx,s in enumerate(count):
        if max_== s:
            result.append(idx+1)
    return result

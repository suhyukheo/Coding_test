def solution(babbling):
    answer = 0
    can_speak= {'aya':'!','ye':'@','woo':'#','ma':'$'}
    
    for i in range(len(babbling)):
        for k,v in can_speak.items():
            babbling[i]=babbling[i].replace(k,v)
            
    for i in range(0,len(babbling)):
        for j in range(0,len(babbling[i])-1):
            if babbling[i][j] == babbling[i][j+1]:
                babbling[i] = "X"*len(babbling[i])
                
    for i in range(len(babbling)):
        for j in ['!','@','#','$']:
            babbling[i] = babbling[i].replace(j,"")
    
    for i in babbling:
        if len(i) == 0:
            answer +=1
            
    return answer 

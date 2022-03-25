
from itertools import product

def solution(word):
    
    dictinary=['A','E','I','O','U']
    result=[]
    count=0
    for i in range(len(dictinary)):
        for w in product(dictinary,repeat=i+1):
            w=list(w)
            w="".join(w)
            result.append(w)
    result.sort()        
    for i in range(len(result)):
        if word==result[i]:
            count=i+1
            
            
    return count
            

                              
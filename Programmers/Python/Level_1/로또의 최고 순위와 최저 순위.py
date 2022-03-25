def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    result=[]
    zero_count=0
    count=0
    for i in lottos:
        if i == 0:
            zero_count+=1
            continue
        else:
            for j in win_nums:
                if i==j:
                    count+=1
                    break
    result.extend([rank[count],rank[zero_count+count]])            
    return result
        
             
        
        
      
def solution(board, moves):
    poket=[]
    count=0
    a=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                poket.append(board[j][i-1])
                board[j][i-1]=0
                a+=1
                if a>=2 and poket[a-2]==poket[a-1]:
                    del poket[a-2:a]
                    count+=2
                    a-=2
                break    
               
    return count
       
        
        
                      
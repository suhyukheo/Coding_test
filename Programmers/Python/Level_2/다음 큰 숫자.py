def solution(n):
    num = bin(n)[2:]
    big_n= n
    n_cnt = 0
    big_n_cnt = 0
    for i in num:
        if i  == "1":
            n_cnt +=1
        else: 
            continue
    while 1:
        if n_cnt == big_n_cnt :
            break
        else:
            big_n_cnt = 0
            big_n+=1
            big_num = bin(big_n)[2:]
            for i in big_num:
                if i == "1":
                    big_n_cnt +=1
                else:
                    continue
            
    return big_n

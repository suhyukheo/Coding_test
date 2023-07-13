def solution(k, tangerine):
    answer = 0
    cnt = 0
    tangerine.sort()
    tangerine_size_dict= {}
    for i in range(tangerine[0],(tangerine[-1]+1)):
         tangerine_size_dict[i] = 0
    for i in tangerine:
        if i in  tangerine_size_dict:
             tangerine_size_dict[i] +=1
    arrange_tangerine_list = sorted(tangerine_size_dict.items(), key=lambda x : x[1], reverse=True)
    for i in arrange_tangerine_list:
        answer+=i[1]
        cnt+=1
        if answer>=k:
            return cnt
    return cnt

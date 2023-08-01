def solution(priorities, location):
    que = [(chr(i+ord('A')),priorities[i]) for i in range(len(priorities))]
    p_cnt = 0 
    q_cnt = 0
    while que:
        a = que.pop(0)
        q_cnt = 0
        for i in que:
            if i[1] > a[1]:
                q_cnt +=1
        if q_cnt >= 1: 
            que.append(a)
        else:
            if ord(a[0])-65 == location:
                p_cnt +=1
                return p_cnt
            else:
                p_cnt+=1
